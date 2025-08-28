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

- **Python 3.12.11+** - Required for modern Django features
- **[uv](https://docs.astral.sh/uv/)** - Recommended for fastest package management
- Alternative: **[copier](https://copier.readthedocs.io/)** - If you prefer traditional pip/pipx

### Step-by-Step Setup

1. **Fork this repository** on GitHub for full customization control
2. **Create your project directory**:
   ```bash
   mkdir my-django-project
   cd my-django-project
   ```
3. **Generate the project** using your fork:
   ```bash
   uvx copier copy https://github.com/your-username/django-copier-template . --trust
   ```
4. **Answer the configuration questions** (or use `--defaults` for quick setup)
5. **Start development** immediately:
   ```bash
   make up      # Start containers
   make migrate # Setup database
   # Your project is ready at http://localhost:8000
   ```

The `.` (dot) means "current directory" - this way you first create and navigate to your desired project folder, then generate the template files directly there instead of creating a nested subdirectory.

### ⚡ Post-Generation Setup

After running the copier command, the template automatically:

1. **Creates environment file** - Renames `.env.example` to `.env` with auto-generated secure credentials
2. **Initializes git** - Sets up git repository with initial commit
3. **Installs dependencies** - Runs `uv sync --all-extras` to install all packages
4. **Configures pre-commit** - Installs and updates pre-commit hooks
5. **Runs quality checks** - Initial code validation with all configured tools
6. **Creates initial commit** - Commits the configured project with descriptive message

**Ready to code immediately** - No additional setup required!

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
make check            # Run pre-commit code checks
make build            # Full build: up + migrations + migrate + admin
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

## 🔐 Security Features

The template prioritizes security with automatic credential generation:

### Auto-Generated Credentials
- **Django Secret Key** - Cryptographically secure 50-character key with special symbols
- **Database Password** - 12-character alphanumeric password
- **Admin Password** - 12-character alphanumeric password for superuser account
- **All credentials** automatically populated in `.env` file during generation

### Security Best Practices
- **No hardcoded secrets** in template or generated code
- **Environment variables** for all sensitive configuration
- **Secure random generation** using Python's `secrets` module
- **Docker security** with non-root containers and minimal attack surface
- **Pre-commit hooks** prevent committing sensitive data

### Generated Credentials Location
After project generation, check your `.env` file for:
```bash
SECRET_KEY=your-auto-generated-secret-key
POSTGRES_PASSWORD=your-auto-generated-db-password
DJANGO_ADMIN_PASSWORD=your-auto-generated-admin-password
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
