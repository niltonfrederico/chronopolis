# Coding Instructions for Chronopolis

## Project Overview

- **Name**: Chronopolis - My own command center
- **Tech Stack**: Django 6.x, NiceGUI 3.x, PostgreSQL (psycopg), Pandas 3.x
- **Python Version**: 3.14+
- **Environment**: Poetry-managed virtual environment

## Core Development Preferences

### Philosophy

- **"Explicit is better than implicit"** - The most important PEP20 Zen principle
- **Security first** - Always prioritize security in code generation
- **PEP8 is law** - Unless preferences explicitly contradict

### Code Style

- **Quotes**: Always prefer double quotes (`"text"` not `'text'`)
- **Typing**: Hard typing user - use type hints extensively
- **Exceptions**: Vanilla exceptions are acceptable when needed
- **Docstrings**: When present, lint them strictly (Google convention)

### Import Organization

- **Style**: Full paths only (no relative imports)
- **Format**: One import per line
- **Priority Order**:
  1. Python built-ins
  2. Known third-party packages (django, nicegui, pandas, psycopg, numpy)
  3. Local modules (chronopolis)
- **Spacing**: 2 lines after imports

### Variable Naming

- **Unused Variables**: Not tolerated, except...
- **Args/Kwargs Pattern**: Variables starting with `_` or `__` can be unused (e.g., `_unused_arg`, `__temp_var`)

## Ruff Configuration

Current setup in `pyproject.toml`:

```toml
[tool.ruff]
line-length = 88
target-version = "py314"
select = ["E", "W", "F", "I", "S", "TC", "D", "Q", "TRY", "C4", "DJ", "PD", "NPY"]
ignore = ["EM101", "EM102", "EM103", "TRY301"]

[tool.ruff.isort]
known-first-party = ["chronopolis"]
known-third-party = ["django", "nicegui", "pandas", "psycopg", "numpy"]
force-single-line = true
lines-after-imports = 2

[tool.ruff.pydocstyle]
convention = "google"

[tool.ruff.flake8-quotes]
docstring-quotes = "double"
inline-quotes = "double"
```

### Enabled Rule Categories

- **E, W**: PEP8 compliance (pycodestyle)
- **F**: Code quality (pyflakes) - includes unused variable detection
- **I**: Import sorting and organization
- **S**: Security rules (flake8-bandit) - comprehensive security linting
- **TC**: Type checking imports
- **D**: Docstring quality (pydocstyle)
- **Q**: Quote consistency
- **TRY**: Exception handling best practices
- **C4**: Comprehension improvements
- **DJ**: Django-specific best practices
- **PD**: Pandas performance and best practices
- **NPY**: NumPy compatibility

## Environment Management

- **Tool**: Poetry
- **Check Environment**: Always run `poetry env info` before creating new environments
- **Dependencies**: Install with `poetry install --with dev`

## Development Workflow

1. **Environment Check**: Verify existing poetry environment before setup
2. **Code Generation**: Follow preferences above
3. **Linting**: Test with `poetry run ruff check`
4. **Validation**: Ensure VSCode schema compliance

## Technology-Specific Guidelines

### Django

- Always include `__str__` methods in models
- Use Django best practices for forms and views
- Prefer explicit over implicit in ORM queries

### NiceGUI

- Follow NiceGUI patterns for UI development
- Maintain clean separation between UI and logic

### Pandas

- Use performance-optimized patterns
- Avoid deprecated functions and methods
- Prefer explicit operations

### PostgreSQL

- Use psycopg for database connections
- Prioritize secure query patterns
- Avoid SQL injection risks

## Security Requirements

- **Priority**: Security is always the top concern
- **Password Handling**: Never hardcode credentials
- **SQL Queries**: Use parameterized queries
- **Input Validation**: Validate all user inputs
- **Dependencies**: Keep security-focused linting enabled

---

*Last Updated: March 14, 2026*
*This file should be consulted and updated whenever generating code for Chronopolis.*
