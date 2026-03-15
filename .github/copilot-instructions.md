# Coding Instructions for Chronopolis

## Project Overview

- **Name**: Chronopolis - My own command center
- **Tech Stack**: Django 6.x, NiceGUI 3.x, PostgreSQL (psycopg), Pandas 3.x
- **Python Version**: 3.14+
- **Environment**: Poetry-managed virtual environment

## Core Development Preferences

### Philosophy

- **"Explicit is better than implicit"** - The most important PEP20 Zen principle
- **Hard typing user** - Always use comprehensive type hints
- **Security first** - Always prioritize security in code generation

### Code Style

- **Quotes**: Always double quotes (`"text"`)
- **Typing**: Extensive type hints required - MyPy strict mode enabled
- **Docstrings**: Google convention when present
- **Imports**: Full paths only, one per line, 2 lines after imports

## Type Checking & Linting

### MyPy Configuration (Strict Mode)

```toml
[tool.mypy]
python_version = "3.14"
strict = true
warn_return_any = true
warn_unused_configs = true
warn_redundant_casts = true
warn_unused_ignores = true
ignore_missing_imports = true
# plugins = ["mypy_django_plugin.main"]  # Enable after Django setup
```

**Type Stubs Installed:**
- `django-stubs` - Django type support
- `types-psycopg2` - PostgreSQL driver types
- `pandas-stubs` - Pandas type support

### Ruff Configuration

```toml
[tool.ruff.lint]
select = ["E", "W", "F", "I", "S", "TC", "D", "Q", "TRY", "C4", "DJ", "PD", "NPY"]
ignore = ["EM101", "EM102", "EM103", "TRY301"]

[tool.ruff.lint.isort]
known-first-party = ["chronopolis"]
known-third-party = ["django", "nicegui", "pandas", "psycopg", "numpy"]
force-single-line = true
lines-after-imports = 2
```

## Development Workflow

1. **Environment Check**: `poetry env info` before setup
2. **Dependencies**: `poetry install --with dev`
3. **Type Check**: `poetry run mypy <file>`
4. **Linting**: `poetry run ruff check <file>`
5. **Auto-fix**: `poetry run ruff check --fix <file>`

## Technology Guidelines

### Type Hints
- All functions must have return type annotations
- Use `Optional[T]` explicitly, never rely on implicit optionals
- Complex types go in `.pyi` files when needed
- No `Any` types unless absolutely necessary

### Django
- Include `__str__` methods in models
- Use explicit ORM queries
- Django stubs will be enabled once project structure exists

### Security
- Never hardcode credentials
- Use parameterized queries
- Validate all user inputs
- Security linting (S rules) always enabled

### Variable Naming
- No unused variables (F rules enforced)
- Exception: variables starting with `_` or `__` can be unused

## AI Usage Guidelines

**IMPORTANT**: All AI assistance must comply with [AI_DISCLAIMER.md](../AI_DISCLAIMER.md)

- If any request violates the AI disclaimer, decline and explain why
- Focus on documentation, configuration, and code completion only
- No large code generation or "vibe coding"
- No user data processing

---

*Optimized for GitHub Copilot with Claude Sonnet 4*
*Last Updated: March 14, 2026*
