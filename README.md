# Django Copier Template

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![Copier](https://img.shields.io/badge/template-copier-blue.svg)](https://copier.readthedocs.io/)

A modern Copier template for Django projects with production-ready tooling and best practices.

## ✨ Features

### 🏗️ Core Framework
- **Django** with environment-based configuration
- **API Framework Choice**: Django Ninja or Django REST Framework
- **Database Support**: PostgreSQL or MySQL
- **Python 3.12+** with modern syntax support

### 🛠️ Development Tools
- **uv** - Fast Python package manager
- **pre-commit** - Git hooks for code quality
- **Linting**: Ruff or Flake8 (configurable)
- **Type Checking**: mypy integration
- **Testing**: pytest with coverage

### 🐳 Production Ready
- **Docker** configuration with multi-stage builds
- **Environment Variables** management with django-environ
- **Settings Split**: Base configuration with environment overrides
- **Custom Management Commands** for enhanced development workflow

### 📁 Project Structure
- **Modular Apps**: Clean separation with `core/apps/` structure
- **API Versioning**: Built-in v1 API structure
- **Custom Shell**: Enhanced Django shell with auto-imports

## 🚀 Quick Start

### Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) (recommended) or [copier](https://copier.readthedocs.io/)

### Using uvx (Recommended)

```bash
uvx copier copy https://github.com/your-username/django-copier-template your-project-name
cd your-project-name
```

### Using copier directly

```bash
pip install copier
copier copy https://github.com/your-username/django-copier-template your-project-name
cd your-project-name
```

## ⚙️ Template Configuration

The template will prompt you for the following options:

| Option | Description | Default | Choices |
|--------|-------------|---------|---------|
| `project_name` | Display name of your project | Django Core Project | - |
| `project_description` | Short description | Auto-generated | - |
| `python_version` | Python version to use | 3.12 | - |
| `api` | API framework | ninja | ninja, drf |
| `db_type` | Database backend | postgresql | postgresql, mysql |
| `linter` | Code linter | ruff | ruff, flake8 |
| `docker_django_port` | Django container port | 8000 | - |

## 🔧 Generated Project Usage

After generation, your project includes a Makefile with common commands:

### Docker Commands
```bash
make up          # Start development containers
make down        # Stop containers
make rebuild     # Full rebuild with cache clearing
make logs        # View container logs
```

### Django Commands
```bash
make migrate     # Apply database migrations
make migrations  # Create new migrations
make admin       # Create superuser
make dj-shell    # Enhanced Django shell
```

### Development Commands
```bash
make pre-commit-check  # Run pre-commit hooks
uv run ruff check      # Lint code
uv run mypy .          # Type checking
uv run pytest         # Run tests
```

## 📂 Generated Structure

```
your-project/
├── core/
│   ├── project/                 # Django settings and config
│   │   ├── settings/
│   │   │   └── base.py         # Environment-based settings
│   │   └── management/
│   │       └── commands/       # Custom management commands
│   └── apps/
│       └── api/                # API application
│           └── v1/             # Versioned API endpoints
├── tests/                      # Test suite
├── docker-compose.yml          # Development containers
├── Dockerfile                  # Production-ready image
├── Makefile                    # Development shortcuts
└── pyproject.toml              # Python project configuration
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Related

- [Django](https://www.djangoproject.com/) - The web framework for perfectionists with deadlines
- [Copier](https://copier.readthedocs.io/) - A library for rendering project templates
- [uv](https://docs.astral.sh/uv/) - An extremely fast Python package installer and resolver
