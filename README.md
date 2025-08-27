# Django Copier Template

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.12.11+-blue.svg)](https://www.python.org/downloads/)
[![Copier](https://img.shields.io/badge/template-copier-blue.svg)](https://copier.readthedocs.io/)

A modern Copier template for Django projects with production-ready tooling and best practices.

## ✨ Features

### 🏗️ Core Framework
- **Django** with environment-based configuration
- **API Framework Choice**: Django Ninja or Django REST Framework
- **Database Support**: PostgreSQL or MySQL
- **Python 3.12.11+** with modern syntax support

### 🛠️ Development Tools
- **uv** - Fast Python package manager
- **pre-commit** - Git hooks for code quality
- **Linting**: Ruff
- **Type Checking**: mypy integration
- **Testing**: pytest with coverage

### 🐳 Production Ready
- **Docker** configuration with optimized multi-stage builds
- **Environment Variables** management with django-environ
- **Settings Split**: Base configuration with environment overrides
- **Custom Management Commands** for enhanced development workflow
- **Security**: Auto-generated secure credentials and secret keys

### 📁 Project Structure
- **Modular Apps**: Clean separation with `core/apps/` structure
- **API Versioning**: Built-in v1 API structure
- **Custom Shell**: Enhanced Django shell with auto-imports
- **Smart App Creation**: Automatic app creation with settings integration

## 🚀 Quick Start

### Prerequisites

- Python 3.12.11+
- [uv](https://docs.astral.sh/uv/) (recommended) or [copier](https://copier.readthedocs.io/)

### **You must fork this repository first**

**Fork this repository on GitHub**, then use your own copy for creating projects:

```bash
uvx copier copy https://github.com/your-username/django-copier-template . --trust
```

The `.` (dot) means "current directory" - this way you first create and navigate to your desired project folder, then generate the template files directly there instead of creating a nested subdirectory.

## ⚙️ Template Configuration

The template will prompt you for the following options:

| Option | Description | Default | Choices |
|--------|-------------|---------|---------|
| `project_name` | Display name of your project | Django Core Project | - |
| `project_description` | Short description | Auto-generated | - |
| `python_version` | Python version to use | 3.12.11 | - |
| `api` | API framework | ninja | ninja, drf |
| `db_type` | Database backend | postgresql | postgresql, mysql |
| `docker_django_port` | Django container port | 8000 | - |

## 🔧 Generated Project Usage

After generation, your project includes a Makefile with common commands:

### Docker Commands
```bash
make up               # Start development containers
make down             # Stop containers
make reset            # Restart containers
make rebuild          # Full rebuild with cache clearing
make clean_volumes    # Stop containers and remove volumes
make logs             # View container logs
```

### Django Commands
```bash
make migrate          # Apply database migrations
make migrations       # Create new migrations
make admin            # Create superuser (uses auto-generated credentials)
make dj_shell         # Enhanced Django shell with auto-imports
make db_shell         # Connect to database shell
make app_name_app     # Create Django app with automatic settings integration
                      # Example: make users_app creates core/apps/users/
                      # and adds "core.apps.users" to LOCAL_APPS
```

### Development Commands
```bash
make pre_commit_check # Run pre-commit hooks
uv run ruff check     # Lint code
uv run mypy .         # Type checking
uv run pytest        # Run tests
```

## 📂 Generated Structure

```
your-project/
├── core/
│   ├── project/                 # Django settings and configuration
│   │   ├── settings/
│   │   │   ├── __init__.py
│   │   │   ├── base.py          # Environment-based settings with LOCAL_APPS
│   │   │   ├── development.py   # Development-specific settings
│   │   │   └── production.py    # Production-specific settings
│   │   ├── management/
│   │   │   └── commands/        # Custom management commands
│   │   │       ├── create_admin.py    # Auto-create superuser
│   │   │       ├── create_app.py      # Smart app creation with settings integration
│   │   │       └── shell.py           # Enhanced Django shell
│   │   ├── urls.py              # Main URL configuration
│   │   ├── wsgi.py              # WSGI application
│   │   └── asgi.py              # ASGI application
│   └── apps/                    # Application modules
│       ├── api/                 # API application (Django Ninja or DRF)
│       │   ├── v1/              # Versioned API endpoints
│       │   │   └── urls.py      # API v1 routes
│       │   ├── schemas.py       # API schemas (if Django Ninja)
│       │   └── urls.py          # API URL configuration
│       └── [your_apps]/         # Apps created with `make app_name_app`
├── .env                         # Environment variables (auto-generated)
├── docker-compose.yml           # Development containers configuration
├── Dockerfile                   # Optimized multi-stage production build
├── Makefile                     # Development command shortcuts
├── manage.py                    # Django management script
├── pyproject.toml              # Python project and dependency configuration
├── .pre-commit-config.yaml     # Pre-commit hooks configuration
└── .gitignore                  # Git ignore patterns
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

Forking this repository gives you:
- Full control over the template
- Ability to customize for your specific needs
- Stable version without unexpected changes
- Freedom to make your own improvements

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Related

- [Django](https://www.djangoproject.com/) - The web framework for perfectionists with deadlines
- [Copier](https://copier.readthedocs.io/) - A library for rendering project templates
- [uv](https://docs.astral.sh/uv/) - An extremely fast Python package installer and resolver
