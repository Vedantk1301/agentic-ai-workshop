"""Print an agent run as a readable trace for the projector.

Shows only what we can actually observe: the tool calls the model asked for,
what the tools returned, and the final answer. It never claims to show the
model's hidden reasoning.
"""

from __future__ import annotations

import json

from langchain_core.messages import AIMessage, HumanMessage, ToolMessage


def _text(message) -> str:
    text = getattr(message, "text", None)
    if isinstance(text, str):
        return str(text)
    if callable(text):  # older langchain-core exposes .text() as a method
        text = text()
    return text if isinstance(text, str) else str(message.content)


def _short(value: str, limit: int = 160) -> str:
    value = " ".join(value.split())
    return value if len(value) <= limit else value[: limit - 3] + "..."


def print_trace(messages, elapsed_seconds: float | None = None, pause: bool = False) -> dict:
    model_calls = 0
    tool_calls = 0
    for message in messages:
        if isinstance(message, HumanMessage):
            print(f"\n[YOU]          {_text(message)}")
        elif isinstance(message, AIMessage):
            model_calls += 1
            if pause:
                input("   (what will the model ask for next? press Enter to reveal) ")
            for call in message.tool_calls:
                tool_calls += 1
                args = ", ".join(f"{k}={json.dumps(v)}" for k, v in call["args"].items())
                print(f"[MODEL ASKS]   {call['name']}({args})")
            text = _text(message).strip()
            if text and not message.tool_calls:
                print(f"[ANSWER]       {text}")
        elif isinstance(message, ToolMessage):
            print(f"[TOOL RESULT]  {_short(str(message.content))}")
    summary = {"model_calls": model_calls, "tool_calls": tool_calls}
    line = f"\n-- {model_calls} model call(s), {tool_calls} tool call(s)"
    if elapsed_seconds is not None:
        summary["seconds"] = round(elapsed_seconds, 1)
        line += f", {elapsed_seconds:.1f}s"
    print(line)
    return summary
