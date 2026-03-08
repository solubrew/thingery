# CODING STANDARDS V9

> **Core Philosophy**: Fail Fast, Fail Clearly. Explicit is better than implicit. Convention over configuration—except when clarity demands otherwise. Keep code concise, performant, configurable, maintainable, and secure.
Only optional packages imports can be put in try except blocks
Internal projects will not ever be import or used as option packages

---

## Project Tasks
- Every Package work session should begin with an update to the projects STATE.md
- Always write CHANGES-<PROJECT>.md files for changes needed in other projects

---

## 1. Project Structure & Workspace

### Standard Project Structure Template
```
project-name/
├── project/
│   ├── __init__.py
│   └── cli.py          # Entry point
├── docs/
│   └── index.md        # Developer Documentation
├── skills/
│   └── project-name/
│       └── SKILL.md
├── tests/
│   ├── unit/
│   ├── integration/
│   └── e2e/
├── README.md            # Project overview and quick start
├── STATE.md             # Current status, work in progress
├── pyproject.toml       # Package metadata and dependencies
├── CHANGES.md           # Changelog (or CHANGES-<project>.md)
├── CODING_STANDARDS.md  # Project coding standards
├── LICENSE              # License file
├── .gitattributes       # Git attributes for LFS, line endings
└── .gitignore           # Git ignore patterns
```

### Shared Workspace (EDN)
```
~/EDN/Documents/SHARED_WORKSPACE/
├── guides/             # Standards and documentation
├── templates/          # Reusable file templates
├── assets/             # Shared images, configs
└── archives/           # Historical versions
```

### Path Discovery Priority (Highest → Lowest)
1. Workspace `projects/` folder
2. Workspace `skills/` folder
3. SHARED_WORKSPACE `~/EDN/Documents/SHARED_WORKSPACE`
4. Python environments in `~/ENVs/`

> **Rule**: Never hardcode absolute paths. Use dynamic workspace resolution.

---

## 2. Import Management

### The tuh Environment (REQUIRED - General)
All agent imports **MUST** use the `tuh` non-GUI virtual environment:
- Core agent dependencies
- CLI tools, data processing, API integrations
- NOT for GUI projects

```bash
source ~/ENVs/tuh/bin/activate
```

### The zuh Environment (REQUIRED - GUI)
All agent GUI imports **MUST** use the `zuh` virtual environment:
- Contains PySide6, PyQt5, and other GUI dependencies
- Use for projects that need desktop GUI (nchantrs, etc.)

```bash
source ~/ENVs/zuh/bin/activate
```

### Python Environment Strategy
```
~/ENVs/
├── tuh   # Core agent dependencies (REQUIRED for CLI/imports)
├── uh    # User-specific customizations
├── truh  # Testing/validation
├── fruh  # Feature development
├── fuh   # Function utilities
└── zuh   # GUI-specific dependencies (PySide6, PyQt5, nchantrs)
```

### Subproject Import Ban (CRITICAL)
> Never import workspace projects as subprojects.

### Dependency Handling
**Fail fast on required dependencies.** Only use try/except for optional packages.

```python
# ❌ Bad - hides missing dependencies
try:
    import required_package
except ImportError:
    pass  # Silently fails later

# ✅ Good - explicit dependency (fails immediately)
import required_package

# ✅ Good - optional dependency
try:
    import optional_package
    HAS_OPTIONAL = True
except ImportError:
    HAS_OPTIONAL = False
```

---

## 3. Git Workflow (MANDATORY)

### Branch Convention
- **Local development**: `local/<agent>-<feature>`
- **Shared integration**: `gamma`
- **Release**: `release/X.Y.Z`

### Agent Git Workflow (CRITICAL RULE)

> **The AGENT will ALWAYS merge FROM gamma TO their `<agent>-ws` branch, never the reverse.**

#### Step-by-Step Workflow:

1. **Start of session**: Merge gamma → `<agent>-ws`
   ```bash
   git checkout morg-ws
   git merge origin/gamma
   ```

2. **Development**: Work on `<agent>-ws` branch

3. **End of session**: Push changes to origin `<agent>-ws`
   ```bash
   git push origin morg-ws
   ```

4. **NEVER**: Merge `<agent>-ws` back to gamma directly

5. **User responsibility**: User reviews and merges agent changes to gamma

### Commit Message Format
```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types**: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

---

## 4. Internal Projects

### Working with Internal Projects
- **DO NOT include internal projects as dependencies in pyproject.toml** - there is an issue with them being registered even on install
- Always attempt to leverage internal projects for features in a project
- Write `CHANGES-<project>.md` files for changes needed in other projects
- Analyze the Project to implement, don't assume implementations

---

## 5. Security & Configuration

### Encryption & Secrets
- **NEVER** show encrypted data or blob contents
- Use `pycurity` for keystore operations

---

## 6. Async Patterns

### Core Guidelines
1. **Await I/O-bound operations**: file reads, network calls, ZMQ
2. **Use `asyncio.to_thread()`** for blocking calls in async context
3. **Never block the event loop**: offload to thread pool

### Error Handling
```python
try:
    result = await risky_operation()
except SpecificError as e:
    logger.error(f"Failed: {e}")
    raise  # Fail fast, fail clearly
```

---

## 7. CLI Implementation

### Use Actual Python CLI Frameworks
**Not bash scripts.** Use `click` or `typer`.

```python
import click

@click.command()
@click.option("--shared", is_flag=True, help="Use shared workspace")
def main(shared):
    workspace = get_workspace(shared)
    # ...
```

---

## 8. Testing Standards

### Test Structure
```
tests/
├── unit/
├── integration/
└── e2e/
```

### Naming Convention
- Unit: `test_<module>_<function>.py`
- Integration: `test_integration_<feature>.py`
- E2E: `test_e2e_<workflow>.py`

---

## 9. Team Coding Rules

### Code Review Checklist
- [ ] Follows naming conventions
- [ ] Has docstrings for public APIs
- [ ] No hardcoded secrets
- [ ] Handles errors explicitly
- [ ] Tests cover happy path AND edge cases
- [ ] No blocking calls in async code
- [ ] Imports use correct environment (tuh or zuh)

---

## 10. Data Formats

| Data Type | Format |
|-----------|--------|
| Config | YAML or JSON |
| Tasks/Projects | AXN or PAXN (YAML) |
| Documents | Native format with clear extension |

---

## 11. Anti-Patterns (DO NOT DO)

### Code Anti-Patterns
| Anti-Pattern | Why | Fix |
|--------------|-----|-----|
| `except: pass` | Swallows all errors | Catch specific exceptions |
| Global state | Unpredictable behavior | Dependency injection |
| Blocking in async | Deadlocks, poor perf | `asyncio.to_thread()` |
| Magic numbers | Unclear intent | Named constants |
| Duplicate code | Maintenance burden | Extract to function |
| Hardcoded paths | Breaks portability | Dynamic resolution |

---

## 12. Environment Variables

| Variable | Purpose |
|----------|---------|
| `<[agent-name]>_WORKSPACE` | Workspace root path |
| `<[agent-name]>_ENV` | Environment name (dev/staging/prod) |
| `<[agent-name]>_AGENT` | Current agent name |

---

## 13. Shared Workspace Guidelines

### Permission Issue Rule (IMPORTANT)
When encountering permission denied errors on shared workspace files:
1. **Default to creating a versioned copy** with `_v{n}` suffix (e.g., `AGENTS_v3.md`)
2. Notify user of the permission issue
3. Provide the new versioned file path
4. Never attempt sudo without explicit user permission

---

## 14. Quick Reference

### Common Commands
```bash
# Activate tuh environment (REQUIRED for imports)
source ~/ENVs/tuh/bin/activate

# Activate zuh environment (REQUIRED for GUI imports)
source ~/ENVs/zuh/bin/activate

# Start of session: merge gamma to agent-ws
git checkout morg-ws
git merge origin/gamma

# End of session: push to agent-ws
git push origin morg-ws
```

---

*Last updated: 2026-03-06*
