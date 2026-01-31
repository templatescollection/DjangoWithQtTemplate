# Django with Qt Template

[![Lint](https://github.com/templatescollection/DjangoWithQtTemplate/actions/workflows/lint.yml/badge.svg)](https://github.com/templatescollection/DjangoWithQtTemplate/actions/workflows/lint.yml)
[![Build](https://github.com/templatescollection/DjangoWithQtTemplate/actions/workflows/build.yml/badge.svg)](https://github.com/templatescollection/DjangoWithQtTemplate/actions/workflows/build.yml)
[![Test](https://github.com/templatescollection/DjangoWithQtTemplate/actions/workflows/test.yml/badge.svg)](https://github.com/templatescollection/DjangoWithQtTemplate/actions/workflows/test.yml)
[![Release](https://github.com/templatescollection/DjangoWithQtTemplate/actions/workflows/release.yml/badge.svg)](https://github.com/templatescollection/DjangoWithQtTemplate/actions/workflows/release.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-6.0+-green.svg)](https://www.djangoproject.com/)
[![PySide6](https://img.shields.io/badge/PySide6-6.10+-informational.svg)](https://doc.qt.io/qt-6/)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![Type checking: mypy](https://img.shields.io/badge/type%20checking-mypy-blue.svg)](https://github.com/python/mypy)
[![Coverage](https://codecov.io/gh/templatescollection/DjangoWithQtTemplate/branch/main/graph/badge.svg)](https://codecov.io/gh/templatescollection/DjangoWithQtTemplate)

A modern full-stack application template with Django REST API backend and PySide6 Qt frontend, built with best practices for production-ready applications.

## 🚀 Features

### Backend
- **Django 6.0+** with Django REST Framework
- **Containerized Deployment** with Docker & Podman
- **Environment-based Configuration** with comprehensive settings management
- **Production-ready** with Gunicorn, Nginx, and health checks
- **Admin Interface** with customizable superuser creation
- **Type Safety** with full MyPy integration
- **Comprehensive Testing** with pytest and Django test suite

### Frontend
- **PySide6** Qt framework for cross-platform desktop applications
- **Qt Designer** UI files with automatic Python generation
- **Modern Styling** with qt-material theming
- **HTTP Client** integrated with backend API

### Shared
- **UV Workspace** for unified dependency management
- **Modern Python Tooling** (Ruff, MyPy, Pre-commit)
- **Task-based Development** with Go-Task automation
- **Code Quality** with automated linting and formatting

## 🛠 Tech Stack

- **Backend**: Django 6.0+, Django REST Framework, Gunicorn
- **Frontend**: PySide6, Qt Designer, qt-material
- **Database**: SQLite (dev), PostgreSQL/MySQL (prod)
- **Deployment**: Docker, Podman, Nginx
- **Development**: UV, Ruff, MyPy, Pre-commit, Go-Task
- **Testing**: pytest, pytest-django

## 📋 Prerequisites

### System Requirements
- **Python**: 3.13+
- **UV**: Modern Python package manager
- **Go-Task**: Task runner for development automation
- **Docker/Podman**: Container runtime
- **Git**: Version control

### Installation
```bash
# Install UV (Python package manager)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install Go-Task
# Linux/macOS
sh -c "$(curl --location https://taskfile.dev/install.sh)" -- -d

# Verify installations
uv --version
task --version
```

## 🚀 Quick Start

### 1. Clone and Setup
```bash
# Clone repository
git clone <repository-url>
cd DjangoWithQtTemplate

# Install workspace dependencies
task install
```

### 2. Configure Environment
```bash
# Copy environment template
cp env.example .env

# Edit environment variables
# Update SECRET_KEY, database settings, etc.
```

### 3. Run Development Servers
```bash
# Start both backend and frontend (in separate terminals)
# Backend:
cd backend
task run

# Frontend:
cd frontend
task run

# Or use root task for instructions
task dev
```

### 4. Access Application
- **Backend API**: http://localhost:8000/
- **Backend Admin**: http://localhost:8000/admin/
- **Frontend**: Desktop application

## ⚙️ Configuration

### Environment Variables

The application uses comprehensive environment-based configuration. Copy `env.example` to `.env` and customize:

```bash
# Core Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1,yourdomain.com
ENVIRONMENT=production

# Database Configuration
DATABASE_URL=postgresql://user:pass@localhost:5432/dbname

# Email Configuration
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# Security Settings
SECURE_SSL_REDIRECT=True
SECURE_HSTS_SECONDS=31536000

# And many more...
```

### Admin User Creation

Create a default admin user for development:

```bash
# From root directory
task backend:createsuperuser

# Or from backend directory
cd backend
task createsuperuser
```

## 📖 Backend API Documentation

### Base URL
```
http://localhost:8000/  (development)
```

### Health Check
```
GET /health/
```
Returns service health status.

### Admin Interface
```
GET /admin/
```
Django admin interface (requires authentication).

## 🖥️ Frontend Development

### UI File Generation

UI files are created with Qt Designer and automatically generated:

```bash
# Generate Python files from .ui files
task frontend:ui-generate

# Check if generated files are up-to-date
task frontend:ui-generate-check
```

### Available Frontend Tasks

```bash
# Frontend operations
task frontend:run         # Run PySide6 application
task frontend:ui-generate # Generate UI Python files
task frontend:lint        # Code linting
task frontend:format      # Code formatting
task frontend:build       # Build package
```

## 🧪 Development

### Available Tasks

```bash
# Root tasks
task install              # Install all workspace dependencies
task all                 # Run all checks (backend + frontend)
task clean               # Clean generated files and caches
task pre-commit          # Run pre-commit hooks on all files

# Backend tasks
task backend             # Show all backend tasks
task backend:run         # Run Django development server
task backend:migrate     # Run database migrations
task backend:test        # Run backend tests
task backend:lint        # Ruff linting
task backend:format      # Ruff formatting
task backend:type-check   # MyPy type checking
task backend:check       # Run all backend checks

# Frontend tasks
task frontend            # Show all frontend tasks
task frontend:run        # Run PySide6 application
task frontend:lint       # Ruff linting
task frontend:format     # Ruff formatting
task frontend:check      # Run all frontend checks
```

### Code Quality

The project uses automated code quality tools:

```bash
# Run all checks
task backend:check
task frontend:check

# Individual tools
task backend:lint        # Ruff linting
task backend:format      # Ruff formatting
task backend:type-check   # MyPy type checking
```

### Pre-commit Hooks

Install pre-commit hooks to run checks automatically on commit:

```bash
# Install hooks
uv run pre-commit install

# Run manually
uv run pre-commit run --all-files
```

### Testing

```bash
# Run all backend tests
task backend:test

# Run with coverage
cd backend && uv run pytest --cov=backend --cov-report=html

# Run specific test
task backend:test-single -- backend/tests/test_basic.py::BasicTestCase::test_admin_url_exists
```

## 🚢 Deployment

### Production Deployment

1. **Build and run containers:**
```bash
docker-compose up --build
```

2. **Scale services:**
```bash
docker-compose up -d --scale backend=3
```

3. **View logs:**
```bash
docker-compose logs -f
```

### Environment Configuration

For production deployment:

1. Set `DEBUG=False`
2. Configure `ALLOWED_HOSTS`
3. Set up proper `SECRET_KEY`
4. Configure production database
5. Enable SSL/TLS settings
6. Set up email configuration

### Health Monitoring

The application includes built-in health checks:

- **Container Health**: Docker health checks
- **Application Health**: Django health endpoints
- **Database Health**: Automatic database connectivity checks

## 📁 Project Structure

```
.
├── pyproject.toml          # UV workspace configuration
├── uv.lock                 # Workspace lock file
├── Taskfile.yml            # Root development tasks
├── .pre-commit-config.yaml  # Pre-commit hooks (root)
├── backend/                # Django backend workspace member
│   ├── backend/            # Django project
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   ├── asgi.py
│   │   └── management/
│   │       └── commands/
│   │           └── createadmin.py
│   ├── tests/              # Backend tests
│   ├── manage.py
│   ├── checkhealth.py
│   ├── entrypoint.prod.sh
│   ├── pyproject.toml      # Backend project config
│   ├── pytest.ini
│   ├── ruff.toml
│   ├── mypy.ini
│   ├── Taskfile.yml        # Backend tasks
│   └── .gitignore
├── frontend/               # PySide6 frontend workspace member
│   ├── src/
│   │   ├── frontend/       # Application code
│   │   │   ├── __init__.py
│   │   │   ├── application.py
│   │   │   └── main_windows.py
│   │   └── ui/            # Generated UI modules
│   │       └── main_windows.py
│   ├── ui/                 # Qt Designer .ui files
│   │   └── MainWindows.ui
│   ├── pyproject.toml      # Frontend project config
│   ├── Taskfile.yml        # Frontend tasks
│   └── .gitignore
├── nginx/
│   └── django.conf        # Nginx configuration
├── .github/workflows/       # GitHub Actions
│   ├── build.yml
│   ├── lint.yml
│   ├── test.yml
│   └── release.yml
├── docker-compose.yml       # Container orchestration
├── env.example             # Environment template
├── .gitignore             # Git ignore rules
├── AGENTS.md              # AI agent guidelines
└── README.md             # This file
```

## 🤝 Contributing

### Development Setup

1. Fork repository
2. Clone your fork: `git clone <your-fork-url>`
3. Set up development environment: `task install`
4. Create feature branch: `git checkout -b feature/your-feature`
5. Make changes and ensure tests pass: `task backend:test`
6. Run quality checks: `task pre-commit`
7. Commit changes: `git commit -m "Add your feature"`
8. Push to your fork: `git push origin feature/your-feature`
9. Create pull request

### Code Standards

- **Linting**: Ruff (PEP 8 compliant)
- **Formatting**: Ruff formatter
- **Type Checking**: MyPy with strict settings
- **Testing**: pytest with Django test framework
- **Commits**: Conventional commits format

### Pull Request Process

1. Ensure all tests pass
2. Update documentation if needed
3. Add tests for new features
4. Follow code style guidelines
5. Get approval from maintainers

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Django Framework
- PySide6 / Qt Framework
- Django REST Framework
- Modern Python tooling ecosystem
- Containerization best practices

---

**Built with ❤️ using Django 6.0+, PySide6, and modern Python practices**
