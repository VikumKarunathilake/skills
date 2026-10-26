# Agent Skills Library

A curated collection of production-ready agent skills for AI coding assistants (Claude Code, Antigravity, Cursor, GitHub Copilot, Codex, Windsurf, and custom LLM agents) compatible with the **[skills.sh](https://skills.sh/)** open ecosystem.

---

## 📦 Quick Installation

Install any skill directly into your current workspace or global agent environment using the official `skills` CLI:

```bash
# Install a specific skill (recommended)
npx skills add VikumKarunathilake/skills --skill better-comments

# Install globally across all supported coding agents
npx skills add VikumKarunathilake/skills --skill better-comments -g

# Install all skills in this repository
npx skills add VikumKarunathilake/skills --all
```

---

## 🛠 Available Skills

| Skill                                            | Category                  | Description                                                                                                                                                   | Quick Command                                                      |
| :----------------------------------------------- | :------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------ | :----------------------------------------------------------------- |
| **[`better-comments`](skills/better-comments/)** | Code Annotation & Quality | Helps AI coding agents write, organize, review, and maintain human-friendly code comments using Better Comments conventions across 20+ programming languages. | `npx skills add VikumKarunathilake/skills --skill better-comments` |

---

## 🌟 Skill Highlights

### `better-comments`

- **Purpose**: Transforms low-value, repetitive AI comments into structured, color-coded annotations that jump out in IDEs (VS Code, Cursor, JetBrains).
- **Core Triggers**:
  - `!` **Alerts / Warnings**: Highlights security hazards, destructive operations, and critical invariants in 🔴 red.
  - `?` **Queries / Questions**: Surfaces ambiguities, design trade-offs, and edge cases to human reviewers in 🔵 blue.
  - `TODO:` **Tasks / Backlog**: Formats actionable work items with clear context and ownership in 🟠 orange.
  - `*` **Highlights / Rationale**: Documents architectural intent (_"why"_, not _"what"_) in 🟢 green.
  - `//` / `DEPRECATED:` **Deprecations**: Strikethrough notation for obsolete code.
- **Documentation**: [skills/better-comments/README.md](skills/better-comments/README.md)
- **Specification**: [skills/better-comments/SKILL.md](skills/better-comments/SKILL.md)

---

## ➕ Adding More Skills in the Future

To add a new skill to this repository:

1. Create a new directory under `skills/<skill-name>/`.
2. Add a `SKILL.md` file with standard YAML frontmatter:
   ```yaml
   ---
   name: your-skill-name
   description: Concise explanation of what the skill does and when an agent should use it.
   license: MIT
   metadata:
     version: "1.0.0"
   ---
   # Skill Title

   Detailed operational instructions, hard rules, and examples...
   ```
3. Add supporting documentation, references, and code examples under `skills/<skill-name>/`.
4. Update the table in this `README.md`.
5. Commit and push to GitHub. The new skill is immediately installable via:
   ```bash
   npx skills add VikumKarunathilake/skills --skill your-skill-name
   ```

---

## 📄 License

This repository is licensed under the [MIT License](LICENSE).
