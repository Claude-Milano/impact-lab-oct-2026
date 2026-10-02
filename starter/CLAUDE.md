# CLAUDE.md for your Impact Lab project

Copy this file into the root of your team repo and edit the parts in angle brackets. Claude Code and Cowork read it as context every time.

---

## What we are building

We are a team at the Claude Impact Lab Milano (3 October 2026), working on Track <01 | 02 | 03>.
The question: how can AI make the City of Milan's services more accessible, for people with disabilities, older people, people who don't speak Italian, people who can't see well?

Our user: <one concrete person, e.g. "an international student who arrived in Milan last week and speaks English and Spanish">.
Our outcome: <one workflow, one outcome>.

## Non-negotiables

- **The solution must run on Claude.** Claude does real work at runtime (understanding, reasoning over rules, asking for what's missing, filling in, routing), through the Claude API. When you propose an architecture, put the Claude call at the core of the user flow, not as decoration.
- **No personal data.** Never generate code that stores or sends real personal data. Use invented cases.
- **A human decides.** Claude proposes; the user or the officer confirms. Show sources for every factual answer about City rules.
- **API keys** live in `.env`, which is in `.gitignore`. Never commit them.
- **Time box:** we have until 16:00. Prefer the simplest stack that demos well. Scope down before polishing.

## Stack

<e.g. Python + FastAPI + a single HTML page; or Next.js; or a Streamlit app>

Runtime model: `claude-sonnet-5-5` by default; `claude-haiku-4-5-20251001` for cheap, high-volume steps such as classification. We have $100 of API credits each: be frugal in loops.

## Data

City open data via the CKAN API at dati.comune.milano.it (see the hub repo's DATA.md). Public service pages on comune.milano.it. Cite every source in the README.

## Definition of done

- The demo works end to end on one realistic, invented case.
- The README follows the template, including "Where Claude works".
- A two-minute screen recording exists.
