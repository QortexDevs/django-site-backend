# Python API Backend

Use this repository as template to start a new Python API Backend

How to use

1. Create new repository via «Use this Template» button on Github

## Project Setup

### 1. Initial Setup

```bash
# Clone repository
git clone <repository-url>
cd django-site-backend

# Build and start containers
docker-compose up --build -d

```

### Running Tests

```bash
# Run all tests
docker exec -it web poetry run pytest

# Run with coverage
docker exec -it web poetry run pytest --cov=src

# Run specific test file
docker exec -it web poetry run pytest tests/test_users.py

# Run tests with verbose output
docker exec -it web poetry run pytest -v
```

### Code Quality

```bash
# Type checking with mypy
docker exec -it web poetry run mypy src

# Linting with ruff
docker exec -it web poetry run ruff check
```

## Poetry Commands with Docker

### 1. Basic Poetry Commands

```bash
# Show current dependencies
docker exec -it web poetry show

# Show dependency tree
docker exec -it web poetry show --tree

# Check for outdated packages
docker exec -it web poetry show --outdated
```

### 2. Adding Dependencies

```bash
# Add single package
docker exec -it web poetry add django

# Add package with extras
docker exec -it web poetry add "pydantic[email]"

# Add multiple packages
docker exec -it web poetry add django gunicorn

# Add package with version constraint
docker exec -it web poetry add "django>=5.0.1"
```

#### Development Dependencies

```bash
# Add to dev group
docker exec -it web poetry add --group dev pytest

# Add multiple dev packages
docker exec -it web poetry add --group dev pytest pytest-asyncio ruff

# Add with extras to dev group
docker exec -it web poetry add --group dev "pytest[asyncio]"
```

### 3. Removing Dependencies

```bash
# Remove main dependency
docker exec -it web poetry remove django

# Remove dev dependency
docker exec -it web poetry remove --group dev pytest
```

### 4. Installing Dependencies

```bash
# Install all dependencies (including dev)
docker exec -it web poetry install

# Install only main dependencies
docker exec -it web poetry install --only main

# Install without dev dependencies
docker exec -it web poetry install --without dev
```

### 5. Updating Dependencies

```bash
# Update all dependencies
docker exec -it web poetry update

# Update specific package
docker exec -it web poetry update django

# Update dev dependencies only
docker exec -it web poetry update --only dev
```

### 6. Lock File Management

```bash
# Generate lock file without installing
docker exec -it web poetry lock

# Update lock file
docker exec -it web poetry lock --no-update

# Check lock file consistency
docker exec -it web poetry check
```

### 7. Virtual Environment Commands

```bash
# Show virtual environment info
docker exec -it web poetry env info

# Show virtual environment path
docker exec -it web poetry env info --path

# Run command in virtual environment
docker exec -it web poetry run python --version

# Run script
docker exec -it web poetry run python src/main.py
```

## Pre-commit

### 1. Installation and Setup

```bash
# Install pre-commit (if not already installed)
pip install pre-commit

# Update pre-commit configuration to latest versions
pre-commit autoupdate

# Install pre-commit hooks
pre-commit install
```

Note: Pre-commit should be installed at the project root level. After installation, hooks will automatically run on every commit.

[Pre-commit docs](https://pre-commit.com/)
