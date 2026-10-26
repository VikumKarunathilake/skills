# Better Comments Skill

Helps AI coding agents write, organize, review, and maintain human-friendly code comments using [Better Comments](https://marketplace.visualstudio.com/items?itemName=aaron-bond.better-comments) annotation conventions across multiple programming languages.

---

## What is this skill?

When AI agents generate or refactor code, comments frequently end up as either non-existent or trivial descriptions of obvious syntax. The `better-comments` skill instructs AI agents to:

1. **Highlight Critical Invariants & Dangers (`!`)**: Red alerts for destructive calls, data mutations, security vulnerabilities, or concurrency pitfalls.
2. **Surface Collaborations & Trade-Offs (`?`)**: Blue queries directly to human reviewers highlighting ambiguities, alternate architectures, or edge cases.
3. **Structure Work Backlog (`TODO:`)**: Orange actionable tasks with clear scope, ownership, or deprecation targets.
4. **Explain Non-Obvious Rationale (`*`)**: Green high-signal commentary answering _"why this approach"_, not _"what this line does"_.
5. **Mark Deprecations (`//` / `DEPRECATED:`)**: Gray strikethrough markers for legacy paths and upcoming removals.

---

## Installation via `npx skills` (skills.sh)

You can install this skill directly into any workspace or AI agent using the standard `skills` CLI:

```bash
# Add to current workspace
npx skills add VikumKarunathilake/skills --skill better-comments

# Or install globally across all coding assistants (Claude Code, Cursor, Antigravity, Copilot)
npx skills add VikumKarunathilake/skills --skill better-comments -g
```

---

## Directory Structure

```
better-comments/
├── SKILL.md                          # Primary agent skill specification & instructions
├── README.md                         # Skill documentation and quickstart
├── references/
│   ├── language-syntax.md            # Syntax reference for 20+ programming languages
│   └── vscode-settings.json          # Recommended VS Code settings for Better Comments
└── examples/
    ├── typescript-example.ts         # TypeScript implementation example
    └── python-example.py             # Python implementation example
```

---

## References

- **VS Code Extension**: [Better Comments by Aaron Bond](https://marketplace.visualstudio.com/items?itemName=aaron-bond.better-comments)
- **Extension Source Code**: [GitHub - aaron-bond/better-comments](https://github.com/aaron-bond/better-comments)
- **Ecosystem**: [skills.sh](https://skills.sh/)
- **Repository**: [GitHub - VikumKarunathilake/skills](https://github.com/VikumKarunathilake/skills)

---

## License

MIT License. Created by [Vikum Karunathilake](https://github.com/VikumKarunathilake).
