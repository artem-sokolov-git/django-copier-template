# Django Copier Template

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.12.11+-blue.svg)](https://www.python.org/downloads/)
[![Copier](https://img.shields.io/badge/template-copier-blue.svg)](https://copier.readthedocs.io/)

> **⚠️ Disclaimer:** This is a hobbyist project created by a beginner developer. While functional and useful for learning, it is not intended as a production-ready solution. You may encounter bugs or suboptimal implementations. Use at your own discretion and feel free to contribute improvements!

A modern Copier template for Django projects with production-ready tooling, custom authentication support, and comprehensive development workflow automation.

## ✨ Features

### 🏗️ Core Framework
- **Django** with environment-based configuration
- **Custom Authentication**: Email or phone-based login with flexible user model
- **API Framework Choice**: Django REST Framework or Django Ninja (optional)
- **Database Support**: PostgreSQL or MySQL
- **Python 3.12.11+** with modern syntax support

### 🔐 Authentication & User Management
- **Flexible Login Fields**: Choose between email or phone authentication
- **Custom User Model**: AbstractUser with email/phone support and validation
- **JSON User Management**: Create users from `data/users.json` file
- **Auto-generated Admin**: Secure admin user creation with random passwords
- **Phone Validation**: E.164 format support for international phone numbers

### 🛠️ Development Tools
- **uv** - Fast Python package manager and virtual environment
- **pre-commit** - Git hooks for automated code quality checks
- **Linting**: Ruff with comprehensive formatting and error detection
- **Type Checking**: ty (fast static type checker replacing mypy)
- **Testing**: pytest with coverage reporting
- **Automated Pipeline**: Complete project initialization with `make pre_build`

### 🐳 Production Ready
- **Docker** configuration with optimized multi-stage builds
- **Environment Variables** management with django-environ
- **Settings Split**: Base configuration with environment-specific overrides
- **Custom Management Commands** for enhanced development workflow
- **Security**: Auto-generated secure credentials and secret keys
- **Requirements Management**: Automated dependency freezing and updates

### 📁 Project Structure
- **Modular Apps**: Clean separation with `core/apps/` structure
- **Conditional API**: Optional API framework with versioned structure
- **Custom Authentication App**: Dedicated `authauth` app when custom auth enabled
- **Data Directory**: JSON-based user fixtures for development
- **Smart App Creation**: Automatic app creation with settings integration

## 🚀 Quick Start

### Prerequisites

- **Python 3.12.11+** - Required for modern Django features
- **[uv](https://docs.astral.sh/uv/)** - Recommended for fastest package management
- Alternative: **[copier](https://copier.readthedocs.io/)** - If you prefer traditional pip/pipx

### Step-by-Step Setup

1. **Fork this repository** on GitHub for full customization control
2. **Generate the project** using your fork:
   ```bash
   uvx copier copy https://github.com/your-username/django-copier-template . --trust
   ```
3. **Answer the configuration questions**:
   - Project name and description
   - Author information
   - Custom authentication preferences (email/phone)
   - API framework choice (DRF/Ninja or none)
   - Database type (PostgreSQL/MySQL)
   - Other customization options

4. **Navigate to your project** and start development:
   ```bash
   cd your-project-slug  # Directory created based on your project name
   make build            # Complete build: containers + migrations + users
   # Your project is ready at http://localhost:8000
   ```

### ⚡ Automated Post-Generation Setup

After running the copier command, the template automatically executes `make pre_build`:

1. **Git Initialization** - Creates git repository and adds all files
2. **Dependency Installation** - Runs `uv sync --all-extras` for all packages
3. **Requirements Freezing** - Generates `requirements.txt` for deployment
4. **Pre-commit Setup** - Installs and updates all code quality hooks
5. **Initial Quality Check** - Runs all linting, formatting, and type checks
6. **Ready to Code** - Project fully configured and validated

**No additional setup required** - Start coding immediately!

## ⚙️ Template Configuration

The template will prompt you for the following options:

### Project Settings
| Option | Description | Default |
|--------|-------------|---------|
| `project_name` | Display name of your project | Django Copier Template |
| `project_description` | Project description | Auto-generated |
| `python_version` | Python version to use | 3.12.11 |

### Author Information
| Option | Description | Default |
|--------|-------------|---------|
| `author_full_name` | Full name of project author | John Doe |
| `author_email` | Author email address | johndoe@email.com |

### Authentication Configuration
| Option | Description | Default | Choices |
|--------|-------------|---------|---------|
| `custom_auth` | Enable custom authentication | true | true, false |
| `auth_login_field` | Login field type | email | email, phone |
| `admin_email` | Administrator email | (author_email) | - |
| `admin_phone` | Administrator phone (if phone auth) | - | E.164 format |

### API and Database
| Option | Description | Default | Choices |
|--------|-------------|---------|---------|
| `api` | Include API framework | true | true, false |
| `api_type` | API framework type | drf | drf, ninja |
| `db_type` | Database backend | postgresql | postgresql, mysql |
| `docker_django_port` | Django container port | 8000 | - |

## 🔧 Generated Project Usage

After generation, your project includes a comprehensive Makefile with development commands:

### Pre-build Pipeline
```bash
make pre_build        # Complete project initialization (auto-run after generation)
make git_init         # Initialize git repository
make uv_sync          # Sync virtual environment with all extras
make requirements_freeze  # Export dependencies to requirements.txt
make install_pre_commit   # Install pre-commit hooks
make autoupdate_pre_commit # Update hook versions
make git_add_all      # Stage all files for git
```

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
make users            # Create users from data/users.json (custom auth)
make superuser        # Create superuser interactively (default auth)
make dj_shell         # Enhanced Django shell with auto-imports
make db_shell         # Connect to database shell
make app_name_app     # Create Django app with automatic settings integration
                      # Example: make users_app creates core/apps/users/
```

### Development Commands
```bash
make build            # Full build: up + migrations + migrate + users/superuser
make check            # Run all quality checks (pre-commit hooks)
uv run ruff check     # Lint code manually
uvx ty check .        # Type checking manually
uv run pytest        # Run tests
```

## 📂 Generated Structure

```
your-project/
├── .env                         # Environment variables with auto-generated secrets
├── .gitignore                   # Git ignore patterns
├── Makefile                     # Development command shortcuts
├── docker-compose.yml           # Development containers
├── Dockerfile                   # Optimized multi-stage production build
├── manage.py                    # Django management script
├── pyproject.toml              # Python project and dependency configuration
├── requirements.txt            # Frozen dependencies for deployment
├── .pre-commit-config.yaml     # Code quality hooks
├── core/
│   ├── project/                # Django settings and configuration
│   │   ├── settings/
│   │   │   ├── base.py         # Environment-based settings with LOCAL_APPS
│   │   │   ├── development.py  # Development-specific settings
│   │   │   └── production.py   # Production-specific settings
│   │   ├── management/
│   │   │   └── commands/       # Custom management commands
│   │   │       ├── create_app.py    # Smart app creation with settings integration
│   │   │       └── shell.py         # Enhanced Django shell
│   │   ├── urls.py             # Main URL configuration
│   │   ├── wsgi.py             # WSGI application
│   │   └── asgi.py             # ASGI application
│   ├── apps/                   # Application modules
│   │   └── authauth/           # Custom authentication app (if custom_auth=true)
│   │       ├── models.py       # Custom User model with email/phone support
│   │       ├── admin.py        # User admin interface
│   │       ├── management/
│   │       │   └── commands/
│   │       │       └── create_users.py  # User creation from JSON
│   │       └── migrations/     # Database migrations
│   └── api/                    # API application (if api=true)
│       ├── v1/                 # Versioned API endpoints
│       │   ├── serializers/    # DRF serializers (if api_type=drf)
│       │   ├── views/          # DRF views (if api_type=drf)
│       │   ├── handlers.py     # Ninja handlers (if api_type=ninja)
│       │   ├── schemas.py      # Ninja schemas (if api_type=ninja)
│       │   └── urls.py         # API v1 routes
│       └── urls.py             # API URL configuration
└── data/
    └── users.json              # User fixtures for custom auth
```

## 🔐 Security Features

The template prioritizes security with comprehensive credential management:

### Auto-Generated Credentials
- **Django Secret Key** - Cryptographically secure 50-character key with special symbols
- **Database Password** - 12-character alphanumeric password
- **Admin Password** - 12-character alphanumeric password for admin user
- **All credentials** automatically populated in `.env` file during generation

### Security Best Practices
- **No hardcoded secrets** in template or generated code
- **Environment variables** for all sensitive configuration
- **Secure random generation** using Python's `secrets` module
- **Docker security** with non-root containers and minimal attack surface
- **Pre-commit hooks** prevent committing sensitive data
- **Phone validation** with E.164 format for international numbers

### Generated Credentials Location
After project generation, check your `.env` file for:
```bash
# Database Configuration
POSTGRES_DB=your_project_db
POSTGRES_USER=your_author_slug
POSTGRES_PASSWORD=auto-generated-12-char-password

# Django Configuration
SECRET_KEY=auto-generated-50-char-secure-key
ENVIRONMENT=development
DOCKER_DJANGO_PORT=8000
```

For custom authentication, also check `data/users.json` for admin user credentials.

## 🔧 Customization

### Adding Custom Apps
Use the smart app creation command:
```bash
make your_app_name_app
```
This automatically:
- Creates `core/apps/your_app_name/` directory
- Adds `"core.apps.your_app_name"` to `LOCAL_APPS` in settings
- Generates standard Django app structure

### Custom Authentication
When `custom_auth=true`, the template provides:
- **Flexible User Model** supporting email or phone authentication
- **Custom UserManager** with validation and normalization
- **Settings Integration** via `AUTH_LOGIN_FIELD`
- **JSON User Creation** from `data/users.json`
- **Admin Interface** adapted for custom fields

### API Development
When `api=true`, choose between:
- **Django REST Framework** - Traditional, mature, extensive ecosystem
- **Django Ninja** - Modern, fast, automatic OpenAPI documentation

Both include versioned URL structure and example endpoints.

## 🐛 Known Issues & Limitations

As this is a hobbyist project by a beginner developer:

- **Limited Testing** - While functional, edge cases may not be covered
- **Performance** - Some configurations may not be optimized for large-scale production
- **Documentation** - Some advanced features may lack comprehensive documentation
- **Dependencies** - Version compatibility issues may arise with future package updates

**Contributions welcome!** If you find bugs or have improvements, please submit issues or pull requests.

## 🤝 Contributing

Contributions are extremely welcome and appreciated! This project benefits from community input.

### How to Contribute
1. **Fork this repository** for your own modifications
2. **Create feature branches** for specific improvements
3. **Submit pull requests** with clear descriptions
4. **Report issues** with detailed reproduction steps
5. **Share feedback** on what works well or could be improved

### Fork Benefits
Forking this repository gives you:
- **Full control** over the template customization
- **Stability** without unexpected changes from upstream
- **Learning opportunity** to understand template mechanics
- **Freedom** to adapt for your specific needs

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Related Resources

- **[Django](https://www.djangoproject.com/)** - The web framework for perfectionists with deadlines
- **[Copier](https://copier.readthedocs.io/)** - A library for rendering project templates
- **[uv](https://docs.astral.sh/uv/)** - An extremely fast Python package installer and resolver
- **[Django REST Framework](https://www.django-rest-framework.org/)** - Powerful and flexible toolkit for building Web APIs
- **[Django Ninja](https://django-ninja.rest-framework.com/)** - Fast Django REST Framework alternative
- **[Ruff](https://docs.astral.sh/ruff/)** - An extremely fast Python linter and code formatter

## ⭐ Support

If you find this template useful, please consider:
- ⭐ **Starring the repository** to show appreciation
- 🐛 **Reporting issues** to help improve the template
- 🔄 **Sharing feedback** on your experience
- 🤝 **Contributing improvements** for the community

Remember: This is a learning project, and your feedback helps make it better for everyone!
