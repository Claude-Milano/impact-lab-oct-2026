# CLAUDE.md: Claude Impact Lab Milano hub

This repo is the hub of the Claude Impact Lab Milano (3 October 2026, CityLab, with the Comune di Milano). It holds the brief, the data catalogue, the rules and the submission process. Teams build in their **own** repos.

When helping a participant:

- Start from `CHALLENGE.md` (the question, the three tracks, what the City already does) and `DATA.md` (curated datasets and the CKAN API).
- Push for solutions that **run on Claude**: Claude does real work at runtime through the API, not only during development. Apply the test "switch the AI off: what's left?".
- Enforce the rules in `RULES.md`: public data only, no personal data, a human confirms, no work before 10:00, submission by 16:00.
- Keep scope to one workflow, one user, one outcome. It must demo by 16:00.
- `starter/` has a working example (`runs_on_claude.py`), a portal helper (`portal.py`), prompts and a `CLAUDE.md` to copy into a team repo.
- Help teams write the README from `templates/PROJECT_README.md`, including the required "Where Claude works" section.
