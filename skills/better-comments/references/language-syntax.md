# Multi-Language Syntax Cheatsheet for Better Comments

Comprehensive reference of comment characters and tag patterns across 20+ programming, markup, and configuration languages.

---

## 1. C-Style Languages

Includes: **TypeScript, JavaScript, C, C++, C#, Java, Go, Rust, PHP, Swift, Kotlin, Dart, Scala**

### Single-Line Comments

```typescript
// ! Alert: Critical warning, invariant, or security boundary
// ? Question: Clarification needed from reviewer or user
// * Highlight: Key algorithm rationale or architectural intent
// TODO: Pending task or future optimization
// FIXME: Known defect or edge-case bug
// NOTE: Important environmental context or constraint
// //// Deprecated or strikethrough code notation
```

### Multi-Line Comments

```typescript
/* !
 * CRITICAL WARNING:
 * Do not modify this memory offset without updating hardware ring buffers.
 */

/* ?
 * Should we enable HTTP/2 push streams here or keep SSE?
 */

/* *
 * Binary search over monotonic timestamps: O(log N) runtime.
 */

/* TODO:
 * Add distributed tracing span attributes for telemetry.
 */
```

---

## 2. Hash-Style Languages

Includes: **Python, Bash / Shell, Ruby, Perl, R, Elixir, Crystal, Dockerfile, YAML, Makefile**

### Single-Line Comments

```python
# ! Alert: Modifies filesystem state directly; ensure backup
# ? Question: Should we cache this DNS response locally?
# * Highlight: Exponential backoff with jitter prevents thundering herd
# TODO: Migrate to asyncio queue once Python 3.12+ baseline is enforced
# FIXME: Memory leak when parsing malformed multipart headers
# NOTE: Uses system CA store rather than certifi bundle
# //// Legacy v1 API wrapper scheduled for removal
```

### Multi-Line / Block Comments (Python Docstring / Bash HereDoc)

```python
"""
! CRITICAL:
Thread-unsafe operation. Must be guarded by acquisition of threading.RLock.
"""
```

---

## 3. SQL & Database Dialects

Includes: **PostgreSQL, MySQL, SQLite, Oracle PL/SQL, Snowflake, BigQuery, Lua, Haskell, Ada**

### Single-Line Comments

```sql
-- ! Alert: Exclusive lock will be held on the users table during this migration
-- ? Question: Can we partition this table by created_at month?
-- * Highlight: Leverages covering index idx_orders_status_created for zero-heap-fetch scans
-- TODO: Add foreign key cascade delete test in staging
-- FIXME: Query planner regression when stats are stale
```

### Multi-Line Comments

```sql
/* !
 * Dropping the view cascades to 3 dependent analytical reporting tables.
 */
```

---

## 4. Web & Markup Languages

Includes: **HTML, XML, SVG, Markdown, Vue / Svelte Template, JSX / TSX**

### HTML / XML / Markdown Comments

```html
<!-- ! Alert: Content Security Policy nonce must be preserved -->
<!-- ? Question: Should we lazy-load this hero video on mobile? -->
<!-- * Highlight: LCP image preloaded in head for 90+ Lighthouse score -->
<!-- TODO: Add WebP and AVIF responsive picture source tags -->
```

### CSS / SCSS / SASS / Less

```css
/* ! Alert: Critical z-index layer reserved for toast notifications */
/* ? Question: Should we replace fixed pixels with CSS clamp() for fluid typography? */
/* * Highlight: Containment property isolates layout repaints to this card */
/* TODO: Purge unused keyframe animations */
```

---

## 5. Shell Scripting & Infrastructure

Includes: **Bash, Zsh, Sh, PowerShell, Terraform / HCL, Nginx Conf**

### PowerShell

```powershell
# ! Alert: Execution requires elevated Administrator privileges
# ? Question: Should we verify code signing certificate before invoking script?
# * Highlight: Queries WMI CIM instances asynchronously
# TODO: Support Nano Server core container image

<#
! Warning:
Terminating error will invoke system trap handler.
#>
```

### Nginx Configuration

```nginx
# ! Alert: Buffer size must match upstream PHP-FPM fastcgi_buffer_size
# * Highlight: HTTP/2 push enabled for critical styles
# ? Question: Should client_max_body_size be increased for video uploads?
# TODO: Add rate limiting zone for /api/v1/auth endpoints
```

### Terraform / HCL

```hcl
# ! Alert: Changing instance_type triggers resource destruction and recreation
# * Highlight: Multi-AZ placement for 99.99% availability SLA
# ? Question: Should we use KMS customer-managed key or AWS managed key?
# TODO: Tag resources with cost-center and environment tags
```
