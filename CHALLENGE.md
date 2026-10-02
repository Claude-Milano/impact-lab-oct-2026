# The challenge

> **How can AI make the City of Milan's services more accessible?**
> For people with disabilities. For older people. For people who don't speak Italian. For people who can't see well.

Accessibility here is meant broadly: not only physical barriers, but access to information, to services, to procedures, in your own language and at your own pace.

## Where this brief comes from

On **9 September 2026** we held a Claude Conversation at Fabbrica del Vapore. Mixed tables, one question. Nine tables wrote down where Milan should start. **This brief is theirs, not ours.**

### What the tables said: six recurring themes

| Tables | Theme | In their words |
|---|---|---|
| 6/9 | **A proactive City** | Reminders instead of fines, alerts on deadlines and duties. *"If the citizen doesn't go to the City, the City reaches the citizen."* |
| 6/9 | **One point of access** | One app, one place that knows you and sends you to the right desk straight away |
| 5/9 | **Onboarding newcomers** | International students, foreigners: tax code, taxes, housing, post office |
| 4/9 | **A City that learns** | Train staff, change agents, listen to the people at the counter |
| 3/9 | **Less bureaucracy** | Thousands of stuck permit files, appointments impossible to find |
| 2/9 | **Mobility and parking** | Permits and area passes, lifts on public transport |

**Fears they named:** privacy and data used without consent, wrong answers (hallucinations), a wider digital divide, losing empathy.
**Brakes they named:** fragmented data and systems that don't talk to each other, inertia, internal skills, data ownership.

Today's rules answer those fears directly: no personal data, and a human always decides.

## What the City already does

From our conversation with the Comune di Milano. **Build on what exists, not next to it**: the jury will recognise a duplicate immediately.

**Already there**
- Automatic emails for new residents and for address changes
- 16 of the 22 most-requested certificates are already online
- A TARI (waste tax) pilot at an advanced stage
- An information path for international students on YesMilano

**Still open**
- How do we know someone has just arrived in the city?
- Useful agents need clean data and reliable connectors
- Systems are fragmented and don't talk to each other

---

## The three tracks

Every team picks **one** track. Inside a track, the idea is yours: these are spaces, not fences.

### Track 01 · Welcome journey for people arriving in Milan
*Came up at 4 of 9 tables. Brings together onboarding, proactivity and a single point of access.*

- **For whom:** new residents, international students, people who don't speak Italian.
- **The job:** tax code, residency, housing, waste tax, transport. What to do, in which order, with which City source.
- **Build on:** the City's existing welcome emails and the YesMilano student path.
- **Claude at work:** an agent that talks or chats in the newcomer's language, reasons over City rules and procedures, and builds a personal checklist with sources.
- **Watch out:** without identity data it can become a smarter FAQ. Show what data and permissions a next version would need to become truly proactive.
- **A day in four steps:** map what a newcomer must do and in what order → design the path of 2–3 concrete people and their critical moments → prototype with Claude (chat and voice, multilingual) over the sources you mapped → design the proactive alerts: which, when, with which data.

### Track 02 · One procedure, assisted from start to submission
*Came up at 2 of 9 tables.*

- **For whom:** citizens and professionals filing with the City.
- **The job:** pick one frequent procedure (a SCIA, a parking permit, a certificate) and take it apart: fields, attachments, typical errors, reasons for rejection.
- **Claude at work:** reads documents and photos, asks only what's missing, pre-fills, and checks everything before submission.
- **Watch out:** a wrong pre-fill falls on the citizen. Claude fills in; the person checks and signs.
- **Measure it:** time and errors with and without the assistant, on 3–5 invented or anonymised cases.

### Track 03 · From inside City Hall: the people at the counter
*Came up at 2 of 9 tables.*

- **For whom:** City staff at service desks and back offices, and through them every citizen they serve.
- **The job:** repeated questions, manual hand-offs, requests that land in the wrong office.
- **Claude at work:** triages incoming requests, routes them, drafts answers with sources for the officer to approve.
- **Why it matters:** it attacks the brakes the tables named most: inertia, culture, internal skills.
- **Watch out:** the benefit to citizens is indirect. Make it visible in your demo.

---

## The test: switch the AI off

| Track | Runs on Claude | Not enough on its own |
|---|---|---|
| 01 · Welcome journey | An agent answers in your language and builds your checklist from City sources | A static page of links and FAQs |
| 02 · Assisted procedure | Reads your documents, asks what is missing, pre-fills and checks the form | A nicer-looking form |
| 03 · Inside City Hall | Classifies and routes requests, drafts sourced replies for the officer | A dashboard of request counts |

If the right-hand column is all that's left, the solution doesn't run on AI yet.

## Problem shapes that fit in a day

From the Impact Lab handbook, useful as inspiration inside any track:

- **Ask the rulebook**: natural-language access to dense rules and procedures.
- **Intake and eligibility**: work out what someone needs or qualifies for, and pre-fill the form.
- **Plain language and translation**: official notices rewritten to be readable, in the languages people speak. Non-technical teammates can lead this one.
- **Triage the inbound queue**: classify, deduplicate and route requests.
- **Messy input to structured record**: a photo or a voice note in, a clean record out.

**Avoid:** anything that needs write access to a live City system, anything that is really a data-cleaning job, and any scope that resolves to "a portal". Push for **one workflow, one user, one outcome**.
