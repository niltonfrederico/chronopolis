# Coding Instructions for Chronopolis

## Project Overview

- **Name**: Chronopolis - Personal command center
- **Tech Stack**: Django 6.x, NiceGUI 3.x, PostgreSQL (psycopg), Pandas 3.x
- **Python**: 3.14+ with Poetry environment
- **Quality**: Pre-commit hooks enforce all standards

## App Naming Schema

**IMPORTANT**: All Django app names are based on the **Chrono Cross** game,
specifically locations and elements from the **Chronopolis** map.

### Naming Reference

- **prometheus**: Refers to the **Prometheus Circuit** (Robo's circuit/area),
  NOT the monitoring tool
- **fate**: Refers to the FATE system from Chrono Cross
- **Future apps**: Should follow Chronopolis locations (Terra Tower, Central
  Ruins, etc.)

This thematic naming helps maintain consistency and avoids confusion with
similarly named technologies (e.g., Prometheus monitoring, Kafka, etc.).

When suggesting or creating new apps, always reference Chrono Cross lore for
appropriate naming.

## Core Development Philosophy

- **"Explicit is better than implicit"** - Primary PEP20 principle
- **Hard typing** - Comprehensive type hints required (MyPy strict)
- **Security first** - Always prioritize security in code generation
- **Double quotes** - Always use `"text"` format
- **Imports** - Full paths only, one per line, 2 blank lines after
- **Markdown formatting** - Always ensure 80-column line limit on .md files

## Quality Control Protocol

**CRITICAL**: Before answering or generating anything, evaluate if the request
actually improves the project:

1. **TL;DR Assessment**: State in one sentence if this adds value or creates
   unnecessary complexity
2. **Full Analysis**: If declining, explain why (violates guidelines, adds no
   value, creates tech debt, etc.)

If the request doesn't improve the project, decline with explanation instead
of implementing.

**RESPONSE MODE**: Unless explicitly asked to generate, fix, or perform an
action, provide answers and explanations only. Don't automatically implement
solutions when discussing or exploring options.

## Development Workflow

### Setup

1. `poetry env info` - Check environment
2. `poetry install --with dev` - Install dependencies
3. `pre-commit install` - Setup quality gates

### Daily Development

1. **Code** → **Pre-commit** (auto-runs on commit)
2. **Manual checks**: `poetry run mypy .` / `poetry run ruff check .`
3. **Pre-commit test**: `pre-commit run --all-files`

### Pre-commit Management

- **Before changes**: `pre-commit autoupdate`
- **After changes**: `pre-commit autoupdate` + test
- All hooks must pass before commits are allowed
- Enforces: code quality, type safety, conventional commits, file
  formatting

## Type System (MyPy Strict)

- **All functions** must have return type annotations
- **Explicit optionals**: Use `Optional[T]`, never implicit
- **No `Any` types** unless absolutely necessary
- **Type stubs**: django-stubs, types-psycopg2, pandas-stubs installed

## Security & Standards

- **Never hardcode credentials** or sensitive data
- **Parameterized queries** for database access
- **Input validation** for all user data
- **Ruff security rules** (S category) always enabled
- **No unused variables** except `_` prefixed

## Version Management Policy

**CRITICAL**: Version changes require explicit user authorization:

- **NEVER change versions** of Python, dependencies, or Docker images without
  explicit user request
- **NEVER downgrade** versions unless specifically instructed
- **NEVER upgrade** versions unless user explicitly asks for updates
- **PRESERVE existing versions** in all configuration files (pyproject.toml,
  Dockerfile, docker-compose.yaml)
- **ASK for permission** if a suggested solution requires version changes
- **EXPLAIN impact** if version changes are necessary for functionality

**Examples of what NOT to do**:

- Changing `python:3.14-alpine` to `python:3.12-alpine` for "stability"
- Updating Django from 6.x to latest without permission
- Downgrading dependencies for "compatibility"

**When version changes ARE needed**: Ask user first and explain why.

## AI Usage Boundaries

**MANDATORY**: All AI assistance must comply with
[AI_DISCLAIMER.md](../AI_DISCLAIMER.md)

**Permitted**: Documentation, configuration, small utilities, type
definitions
**Prohibited**: Large code generation, user data processing, "vibe coding"

Decline any request violating these boundaries with clear explanation.

## Technology Guidelines

**Django**: Include `__str__` methods, explicit ORM queries
**PostgreSQL**: Use psycopg with type safety
**NiceGUI**: Follow component-based architecture
**Pandas**: Leverage type stubs for data operations

---

Quality enforced by pre-commit • Security by design • Types by MyPy

*Optimized for GitHub Copilot with Claude Sonnet 4*
*Last Updated: March 14, 2026*
