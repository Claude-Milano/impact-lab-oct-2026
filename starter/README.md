# Starter kit

| File | What it is |
|---|---|
| [PROMPTS.md](PROMPTS.md) | Prompts to pick the problem, design the journey, design where Claude works, build and pitch |
| [CLAUDE.md](CLAUDE.md) | A `CLAUDE.md` to copy into your team repo, with the day's non-negotiables |
| [runs_on_claude.py](runs_on_claude.py) | A minimal solution that runs on Claude: it answers in the user's language and searches City open data by itself, through tool use |
| [portal.py](portal.py) | A tiny helper to search, inspect and download datasets from dati.comune.milano.it |

```bash
cd starter
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env                 # add your ANTHROPIC_API_KEY
python portal.py search residenza
python runs_on_claude.py "I just moved to Milan, where is the nearest registry office to Città Studi?"
```

This is a starting point, not a solution. Copy the pattern, not the code: one system prompt, a few tools that reach your sources, a loop, and a human who confirms.
