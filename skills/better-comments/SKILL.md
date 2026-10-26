---
name: better-comments
description: Helps AI coding agents write, organize, review, and maintain human-friendly code comments using Better Comments annotation conventions across multiple programming languages. Use when writing code comments, refactoring legacy comments, explaining complex algorithms, marking critical security alerts, leaving review queries for human engineers, or organizing technical debt and TODOs.
license: MIT
metadata:
  version: "1.0.0"
  author: "Vikum Karunathilake"
  homepage: "https://github.com/VikumKarunathilake/skills"
  references:
    - name: "Better Comments VS Code Marketplace"
      url: "https://marketplace.visualstudio.com/items?itemName=aaron-bond.better-comments"
    - name: "Better Comments GitHub Repository"
      url: "https://github.com/aaron-bond/better-comments"
---

# Better Comments for AI Coding Agents

Transform ordinary code comments into visually structured, high-signal annotations that stand out in human IDEs (VS Code, Cursor, JetBrains) using the [Better Comments](https://marketplace.visualstudio.com/items?itemName=aaron-bond.better-comments) convention.

As an AI coding agent, your comments must provide immediate visual clarity to human developers reviewing diffs and inspecting source files.

---

## The 5 Core Better Comments Categories

Every comment written or refactored under this convention must begin with one of the standard categorization triggers immediately following the language's comment delimiter:

| Category                       | Trigger Prefix        | VS Code Color Theme  | Purpose & Intent                                                                                        | When to Use                                                                                                        |
| :----------------------------- | :-------------------- | :------------------- | :------------------------------------------------------------------------------------------------------ | :----------------------------------------------------------------------------------------------------------------- |
| **Alert / Warning**            | `!`                   | Red                  | High-risk behaviors, security implications, destructive calls, invariants, critical preconditions.      | Database drops, external process kills, security traps, non-idempotent operations, unvalidated inputs.             |
| **Query / Clarification**      | `?`                   | Blue                 | Solicits human reviewer input, highlights ambiguities, unresolved edge cases, architectural trade-offs. | Uncertainty in user intent, missing requirements, performance vs. memory trade-offs, potential future bottlenecks. |
| **Task / Backlog**             | `TODO:` or `TODO`     | Orange               | Actionable work items, pending refactors, scheduled integrations, planned feature follow-ups.           | Deferred optimizations, upcoming API migrations, unit test gaps.                                                   |
| **Highlight / Intent**         | `*`                   | Green                | Core algorithmic insights, architectural decisions, business logic rationale (_"why"_, not _"what"_).   | Non-obvious mathematical steps, regex explanations, workflow dispatch rationale, complex state transitions.        |
| **Deprecated / Strikethrough** | `//` or `DEPRECATED:` | Strikethrough (Gray) | Deprecated functions, obsolete parameters, dead code scheduled for removal.                             | Legacy endpoints, backward-compatibility shims, superseded configurations.                                         |

### Extended Industry Tags (Commonly Configured)

When the project context or team standards warrant additional granularity:

- **`FIXME:` / `BUG:`**: Known defect or edge case anomaly requiring an upstream fix.
- **`NOTE:` / `INFO:`**: Onboarding context, API quirks, or non-obvious environmental dependencies.
- **`HACK:`**: Intentional temporary workaround for an external library bug or protocol limitation.
- **`PERF:`**: Performance-critical section with micro-optimization justifications.

---

## Multi-Language Comment Syntax Matrix

Ensure the prefix is placed immediately after the comment delimiter and a single space:

| Language Family               | Single-Line Syntax   | Block / Multi-Line Syntax    | Example                                                                                                               |
| :---------------------------- | :------------------- | :--------------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| **TypeScript / JavaScript**   | `// <prefix> <text>` | `/* <prefix> <text> */`      | `// ! Never expose credentials in client-side bundles`<br>`// * Memoizes compute-heavy diff trees`                    |
| **Python**                    | `# <prefix> <text>`  | `""" <prefix> <text> """`    | `# ! Requires superuser privilege`<br>`# ? Should we fallback to memory cache if Redis is down?`                      |
| **Go**                        | `// <prefix> <text>` | `/* <prefix> <text> */`      | `// ! Goroutine leak hazard if context is not cancelled`<br>`// * Idempotent retry loop with exponential backoff`     |
| **Rust**                      | `// <prefix> <text>` | `/* <prefix> <text> */`      | `// ! Unsafe block: pointer must remain non-null`<br>`// TODO: Replace with NonNull<T> in v2`                         |
| **C / C++ / C# / Java**       | `// <prefix> <text>` | `/* <prefix> <text> */`      | `// ! Freeing buffer before socket flush causes packet loss`<br>`// * Aligned on 64-byte cache lines`                 |
| **Bash / Shell / PowerShell** | `# <prefix> <text>`  | `<# <prefix> <text> #>` (PS) | `# ! Destructive: removes orphaned Docker volumes`<br>`# * Fallback to curl if wget is unavailable`                   |
| **SQL**                       | `-- <prefix> <text>` | `/* <prefix> <text> */`      | `-- ! Concurrent index creation requires exclusive table lock`<br>`-- * Uses partial index for active tenant queries` |
| **HTML / XML / SVG**          | N/A                  | `<!-- <prefix> <text> -->`   | `<!-- ! Do not remove nonce placeholder for CSP -->`<br>`<!-- TODO: Migrate to responsive picture tags -->`           |
| **CSS / SCSS / Less**         | N/A                  | `/* <prefix> <text> */`      | `/* ! Z-index stacking context required for modal overlay */`<br>`/* * Hardware acceleration trigger */`              |
| **YAML / Dockerfile**         | `# <prefix> <text>`  | N/A                          | `# ! Hard memory limit strictly enforced by cgroups`<br>`# * Health check probe with 5s timeout`                      |

---

## AI Agent Operational Protocols

### Rule 1: Signal-Over-Noise (Never Comment the Obvious)

**Anti-Pattern (Restating Code)**:

```typescript
// * Set counter to 0
let counter = 0;

// * Loop over items
for (const item of items) {
  // * Log item
  console.log(item);
}
```

**Production Standard (Explaining Rationale & Invariants)**:

```typescript
// * Reset counter before each batch window to prevent buffer overflow in stream consumers
let counter = 0;

// ! Batch size must not exceed 500 items to avoid triggering upstream HTTP 413
for (const item of items) {
  // * Dispatches asynchronously to avoid blocking the main event loop
  void processItemAsync(item);
}
```

### Rule 2: Precision Spacing & Formatting

- **Correct**: `// ! Warning message`
- **Incorrect**: `//!Warning message` (fails tag detection in most regex engines)
- **Incorrect**: `//   ! Warning message` (excessive whitespace may break parser)

### Rule 3: Use `?` for Reviewer Collaboration

When generating code where multiple trade-offs exist or requirements are partially ambiguous:

```typescript
// ? Should we emit a webhook event here, or rely solely on database CDC listeners?
// ? If the downstream microservice is unreachable, should we queue in dead-letter or fail immediately?
```

This enables the user or reviewer to immediately spot architectural questions during code review.

### Rule 4: Actionable `TODO:` with Ownership and Scope

Never leave a bare `// TODO`. Always provide context and clear success criteria:

```typescript
// TODO: Replace naive linear search with binary search once item list exceeds 10,000 records.
// TODO(auth): Support Ed25519 public key verification once dependency upgrade lands in v2.4.
```

### Rule 5: Distinguish Docstrings from Better Comments

- **Docstrings (`/** ... \*/`/`""" ... """`)\*\*: Intended for public API contracts, parameter types, and external callers.
- **Better Comments (`// !`, `// *`, `# !`)**: Intended for internal implementation details, risk warnings, reviewer inquiries, and technical debt inside function bodies.

---

## Concrete Code Demonstrations

### TypeScript / JavaScript Example

```typescript
class SessionTokenVault {
  private cache = new Map<string, TokenMetadata>();

  /**
   * Refreshes an active session token.
   */
  public async refreshToken(sessionId: string): Promise<string> {
    // ! CRITICAL: Ensure token signature is validated BEFORE updating in-memory cache
    if (!this.isValidSession(sessionId)) {
      throw new UnauthorizedError("Session validation failed");
    }

    // * Atomic check-and-swap prevents race conditions across concurrent refresh requests
    const active = this.cache.get(sessionId);
    if (active?.isRefreshing) {
      // ? Should we return the existing in-flight promise rather than polling?
      return this.waitForInFlightToken(sessionId);
    }

    // TODO: Migrate token storage to Redis cluster once multi-instance horizontal scaling is deployed
    const newToken = await this.cryptoSign(sessionId);

    // //// Legacy HMAC-SHA1 fallback removed in favor of Ed25519
    return newToken;
  }
}
```

### Python Example

```python
def execute_database_migration(connection_pool, target_version: int):
    # ! DANGER: Modifies table schema in-place. Verify snapshot backup exists before invocation.
    if not verify_backup_status():
        raise BackupNotFoundError("Migration aborted: verified backup not detected.")

    # * Uses advisory locks to guarantee single-runner execution across distributed workers
    with connection_pool.get_advisory_lock(MIGRATION_LOCK_ID):
        # ? Should we support dry-run mode via an environment variable flag?
        current_version = get_schema_version(connection_pool)

        # TODO: Add progress telemetry callback for long-running index migrations
        if current_version < target_version:
            apply_migration_scripts(connection_pool, current_version, target_version)
```

---

## Verification & Self-Correction Checklist

Before delivering or committing code, inspect all generated comments:

1. [ ] Does every non-docstring comment start with a valid tag (`!`, `?`, `*`, `TODO:`, `//`)?
2. [ ] Is there exactly one space after the comment delimiter and before the tag?
3. [ ] Are destructive operations and security boundaries highlighted with `!`?
4. [ ] Are unclarified assumptions or edge cases tagged with `?` for human review?
5. [ ] Are obvious tautological comments ("increment counter", "return value") eliminated?

---

## References & Documentation Links

### Official Extension & Upstream Source
- **VS Code Marketplace**: [Better Comments by Aaron Bond](https://marketplace.visualstudio.com/items?itemName=aaron-bond.better-comments)
- **GitHub Repository**: [aaron-bond/better-comments](https://github.com/aaron-bond/better-comments)

### Skill Reference Guides & Assets
- **Syntax Cheatsheet**: [Multi-Language Syntax Reference (20+ Languages)](references/language-syntax.md)
- **VS Code Configuration**: [Recommended VS Code settings.json](references/vscode-settings.json)
- **Code Demonstrations**:
  - [TypeScript Implementation Demonstration](examples/typescript-example.ts)
  - [Python Implementation Demonstration](examples/python-example.py)

### Agent Ecosystem & Registry
- **Skills Directory**: [skills.sh](https://skills.sh/)
- **Skills Source Repository**: [GitHub: VikumKarunathilake/skills](https://github.com/VikumKarunathilake/skills)
