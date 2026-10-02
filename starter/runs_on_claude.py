"""A minimal example of a solution that RUNS ON CLAUDE.

A newcomer asks a question in any language. At runtime Claude:
  1. understands the question and the language,
  2. decides by itself to search the City's open data portal (a tool),
  3. answers in the user's language, citing the datasets it used,
  4. says what a human should double-check.

This is a starting point, not a solution: replace the tool with the sources
your track needs (City pages, a dataset, a form checker...).

    pip install -r requirements.txt
    cp .env.example .env          # add your ANTHROPIC_API_KEY
    python runs_on_claude.py "Dove posso fare la carta d'identità vicino a Lambrate?"
    python runs_on_claude.py "I just moved to Milan as a student, where is the nearest registry office?"
"""
import json
import os
import sys

import anthropic
from dotenv import load_dotenv

from portal import search, show

load_dotenv()
client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY

# Sonnet for the conversation. Use claude-haiku-4-5-20251001 for cheap, high-volume steps.
MODEL = os.getenv("CLAUDE_MODEL", "claude-sonnet-5-5")

SYSTEM = """You help people use the services of the Comune di Milano: newcomers,
older people, people with disabilities, people who don't speak Italian.
- Always answer in the language the user wrote in, in plain words.
- Use the tools to find City data before answering factual questions. Never invent
  addresses, rules, deadlines or opening hours.
- Cite the datasets you used (slug and title).
- End with one line on what the person should double-check with the City, and how.
- Never ask for or store personal data."""

TOOLS = [
    {
        "name": "search_city_datasets",
        "description": "Search the Comune di Milano open data portal. Returns dataset slugs and titles.",
        "input_schema": {
            "type": "object",
            "properties": {"query": {"type": "string", "description": "Italian keywords work best, e.g. 'sedi anagrafici'"}},
            "required": ["query"],
        },
    },
    {
        "name": "get_city_dataset",
        "description": "Get the description and download links of one dataset by slug.",
        "input_schema": {
            "type": "object",
            "properties": {"slug": {"type": "string"}},
            "required": ["slug"],
        },
    },
]


def run_tool(name: str, args: dict) -> str:
    try:
        if name == "search_city_datasets":
            return json.dumps(search(args["query"], rows=10), ensure_ascii=False)
        if name == "get_city_dataset":
            return json.dumps(show(args["slug"]), ensure_ascii=False)[:8000]
        return f"Unknown tool {name}"
    except Exception as e:  # report errors back to Claude instead of crashing
        return f"Tool error: {e}"


def ask(question: str, max_turns: int = 6) -> str:
    messages = [{"role": "user", "content": question}]
    for _ in range(max_turns):
        response = client.messages.create(
            model=MODEL, max_tokens=1500, system=SYSTEM, tools=TOOLS, messages=messages
        )
        messages.append({"role": "assistant", "content": response.content})
        if response.stop_reason != "tool_use":
            return "".join(b.text for b in response.content if b.type == "text")
        results = [
            {"type": "tool_result", "tool_use_id": b.id, "content": run_tool(b.name, b.input)}
            for b in response.content
            if b.type == "tool_use"
        ]
        messages.append({"role": "user", "content": results})
    return "Stopped after too many steps."


if __name__ == "__main__":
    print(ask(" ".join(sys.argv[1:]) or "Where can I get a certificate of residence in Milan?"))
