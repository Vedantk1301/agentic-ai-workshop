"""Run this the night before: checks Python, packages, your key and one Gemini call.

  .venv\\Scripts\\python starter/check_setup.py

It never prints your key.
"""

from __future__ import annotations

import os
import sys
from importlib.metadata import version

from dotenv import load_dotenv

from canteen import console, models


def main() -> None:
    console.setup()
    print(f"Python {sys.version.split()[0]}")
    for pkg in ("langchain", "langgraph", "langchain-google-genai", "google-genai"):
        print(f"  {pkg:<24}{version(pkg)}")

    load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))
    key = os.environ.get("GOOGLE_API_KEY", "")
    if not key:
        print("\nNo GOOGLE_API_KEY in .env yet. Offline demos still work (--offline).")
        return
    print(f"\nKey found ({len(key)} characters). Model: {os.environ.get('GEMINI_MODEL', models.DEFAULT_MODEL)}")

    from google import genai

    client = genai.Client(api_key=key)
    flash = []
    for m in client.models.list():
        actions = getattr(m, "supported_actions", None) or []
        if "flash" in m.name and (not actions or "generateContent" in actions):
            flash.append(m.name.replace("models/", ""))
    print("Flash models your key can see:", ", ".join(sorted(flash)[-8:]) or "(none listed)")

    reply = models.live_model().invoke("Reply with exactly: canteen ready")
    print("Test call says:", getattr(reply, "text", reply.content))
    print("\nAll good. If the test call failed with a model error, set GEMINI_MODEL in .env to one listed above.")


if __name__ == "__main__":
    main()
