"""Which "brain" the agent demos use.

  live     Gemini through LangChain. Needs GOOGLE_API_KEY in the project's .env.
  offline  A rule-based stand-in that follows the same think-act-observe loop.
           Use it when the Wi-Fi or the free quota dies. It is NOT a real AI:
           say so on stage ("this is my offline stand-in, same loop").
"""

from __future__ import annotations

import json
import os
from typing import Any

from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import AIMessage, HumanMessage, ToolMessage
from langchain_core.outputs import ChatGeneration, ChatResult

from canteen import answers, rules

DEFAULT_MODEL = "gemini-3.6-flash"


def live_model():
    from dotenv import load_dotenv
    from langchain_google_genai import ChatGoogleGenerativeAI

    load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))
    if not os.environ.get("GOOGLE_API_KEY"):
        raise SystemExit(
            "No GOOGLE_API_KEY found. Copy .env.example to .env and paste your free key "
            "from Google AI Studio, or run with --offline."
        )
    return ChatGoogleGenerativeAI(
        model=os.environ.get("GEMINI_MODEL", DEFAULT_MODEL),
        temperature=0,
        max_retries=2,
        timeout=30,
    )


class OfflineStandIn(BaseChatModel):
    """Rule-based stand-in for a tool-calling model (offline backup + tests)."""

    bound_tool_names: list[str] = []

    @property
    def _llm_type(self) -> str:
        return "offline-stand-in"

    def bind_tools(self, tools, **kwargs: Any) -> "OfflineStandIn":
        names = []
        for t in tools:
            name = getattr(t, "name", None)
            if name is None and isinstance(t, dict):
                name = t.get("name") or t.get("function", {}).get("name")
            if name is None and isinstance(t, type):
                name = t.__name__
            names.append(name)
        return self.model_copy(update={"bound_tool_names": names})

    def _generate(self, messages, stop=None, run_manager=None, **kwargs: Any) -> ChatResult:
        return ChatResult(generations=[ChatGeneration(message=self._next(messages))])

    def _next(self, messages) -> AIMessage:
        question = next(m.content for m in messages if isinstance(m, HumanMessage))
        wanted = rules.extract_constraints(question)
        asked = {}
        for m in messages:
            if isinstance(m, AIMessage):
                for call in m.tool_calls:
                    asked[call["id"]] = call["name"]
        results = {}
        for m in messages:
            if isinstance(m, ToolMessage):
                results[asked.get(m.tool_call_id, m.name)] = json.loads(m.content)

        def call(name: str, args: dict) -> AIMessage:
            return AIMessage(content="", tool_calls=[{"name": name, "args": args, "id": f"call_{len(asked) + 1}"}])

        if wanted["budget"] and "find_food" not in results and "find_food" in self.bound_tool_names:
            return call("find_food", {"max_price": wanted["budget"], "vegetarian": wanted["vegetarian"]})
        if wanted["wants_hours"] and "get_canteen_hours" not in results and "get_canteen_hours" in self.bound_tool_names:
            return call("get_canteen_hours", {})
        if wanted["wants_refund"] and "get_refund_policy" not in results and "get_refund_policy" in self.bound_tool_names:
            return call("get_refund_policy", {})

        menu = results.get("find_food")
        parts = []
        if not wanted["budget"]:
            parts.append("What's your budget? I'll check what's in stock under it.")
        elif menu is not None:
            error = menu.get("error") if menu.get("status") == "error" else None
            parts.append(answers.menu_sentence(wanted, None if error else menu, error))
        if "get_canteen_hours" in results:
            parts.append(answers.hours_sentence(results["get_canteen_hours"]))
        if "get_refund_policy" in results:
            policy = results["get_refund_policy"]
            error = policy.get("error") if policy.get("status") == "error" else None
            parts.append(answers.policy_sentence(None if error else policy, error))
        text = " ".join(parts) or "I can help with the menu, prices, stock, hours and refunds."

        schema_tools = [n for n in self.bound_tool_names if n and n[0].isupper()]
        if schema_tools:  # structured answer requested (used by 04_graph_with_agent.py)
            recommended = [m["name"] for m in (menu or {}).get("matches", [])]
            return call(schema_tools[0], {"recommended_dishes": recommended, "message": text})
        return AIMessage(content=text)


def get_model(offline: bool):
    return OfflineStandIn() if offline else live_model()
