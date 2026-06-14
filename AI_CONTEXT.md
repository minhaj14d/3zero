# AI_CONTEXT.md — 3 Zero Progress Index

Portable memory for Claude, ChatGPT, Gemini, Aider, Roo, Cline, OpenHands.

## Project Summary

**3 Zero Progress Index** — Bangladesh 3 Zero Movement composite index (3ZPI) — poverty, unemployment, carbon. Path: `D:\Workflow\3zero`. Status: active, ~75%.

## Current Priorities

1. Read PROJECT_STATE.md before coding
2. Do not refactor unrelated modules
3. Update docs when behavior changes

## Important Files

- README (if exists)
- `research-notes/{data` 
- Config: package.json / pyproject.toml / build.gradle.kts

## Critical Design Decisions

- Stack locked to: Python, pandas, wbgapi, LaTeX
- Same author track as researchonthego, math

## Do Not Change Rules

- No secrets in git
- No force-push to main
- No breaking API changes without migration notes
- For IME projects: do not modify upstream core without fork documentation

## Coding Patterns

- Match existing file naming and import style
- Prefer extending existing modules over new abstractions
- Run linter/tests before claiming done

## Common Mistakes

- Assuming Supabase/env vars are set (many projects use fallbacks)
- Editing upstream OSS without checking fork vs upstream boundary
- Duplicating Avro parser logic — check avro.py / fcitx5 tools first

## Future Vision

Policy-relevant composite index for Bangladesh sustainable development. → production-ready, linked from portfolio-4.

## Recommended Development Workflow

1. `cd D:\Workflow\3zero`
2. Read README + AI_CONTEXT.md
3. Create branch, small commits
4. Update PROJECT_STATE.md when done
5. Cross-link in knowledge-os if significant decision
