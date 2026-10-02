# Starter prompts

Use these with Claude (claude.ai, Cowork or Claude Code). Paste the hub repo's `CHALLENGE.md` and `DATA.md` first, or open the repo with Claude so it has them as context.

## 1. Pick the problem (first 20 minutes)

```
We are a team of <n> at the Claude Impact Lab Milano, Track <01|02|03>.
Our skills: <design, code, domain knowledge...>.
Using CHALLENGE.md and DATA.md, propose 5 problems we could solve in 5 hours.
For each: the user (one concrete person), the moment they get stuck, what Claude
would do at runtime, which City sources we'd use, and the biggest risk.
Then challenge them: which ones would fail the "switch the AI off" test?
Rank them by day-one impact for the Comune.
```

## 2. Design the user journey

```
Our user is <persona>. Walk through their journey from <trigger> to <outcome>
step by step. For each step: what they see, what they do, what Claude does,
what a human confirms, and which source backs Claude's answer.
Flag the steps where a wrong answer would hurt them.
```

## 3. Design where Claude works

```
Design the runtime role of Claude in our solution: the system prompt, the tools
it needs (e.g. search City pages, read a dataset, check a form), what it may
decide alone and what it must ask a human to confirm.
Keep it to the smallest design that demos well by 16:00.
Then write the "Where Claude works" section of our README.
```

## 4. Plain language and multilingual

```
Rewrite this City page for <persona>, in <language>, at a reading level a
14-year-old could follow. Keep every rule and deadline exact, list what you
simplified, and link the original. <paste page text>
```

## 5. Build the prototype

```
Read CLAUDE.md. Build the smallest working version of <solution>:
<stack>. One page, one flow, one invented user case.
Put the Claude API call at the core of the flow. Keep the API key in .env.
After each step, tell me how to run it.
```

## 6. Prepare the pitch

```
Write a 2-minute pitch in four beats: the problem (20s), the demo (60s),
where Claude works (20s), day one for the City (20s).
Then list the 3 questions the jury from the Comune is most likely to ask, and
our honest answers.
```
