# Backend

[![Build](https://github.com/templatescollection/DjangoTemplate/actions/workflows/build.yml/badge.svg)](https://github.com/templatescollection/DjangoTemplate/actions/workflows/build.yml)
[![CI](https://github.com/templatescollection/DjangoTemplate/actions/workflows/ci.yml/badge.svg)](https://github.com/templatescollection/DjangoTemplate/actions/workflows/ci.yml)
[![Lint](https://github.com/templatescollection/DjangoTemplate/actions/workflows/lint.yml/badge.svg)](https://github.com/templatescollection/DjangoTemplate/actions/workflows/lint.yml)
[![Test](https://github.com/templatescollection/DjangoTemplate/actions/workflows/test.yml/badge.svg)](https://github.com/templatescollection/DjangoTemplate/actions/workflows/test.yml)
[![Release](https://github.com/templatescollection/DjangoTemplate/actions/workflows/release.yml/badge.svg)](https://github.com/templatescollection/DjangoTemplate/actions/workflows/release.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-6.0+-green.svg)](https://www.djangoproject.com/)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![Type checking: mypy](https://img.shields.io/badge/type%20checking-mypy-blue.svg)](https://github.com/python/mypy)
[![Coverage](https://codecov.io/gh/templatescollection/DjangoTemplate/branch/main/graph/badge.svg)](https://codecov.io/gh/templatescollection/DjangoTemplate)

A modern Django REST API backend with containerized deployment, built with best practices for production-ready applications.

## 🚀 Features

- **Django 6.0+** with Django REST Framework
- **Containerized Deployment** with Docker & Podman
- **Environment-based Configuration** with comprehensive settings management
- **Modern Python Tooling** (UV, Ruff, MyPy, Pre-commit)
- **Task-based Development** with Go-Task automation
- **Production-ready** with Gunicorn, Nginx, and health checks
- **Comprehensive Testing** with pytest and Django test suite
- **Admin Interface** with customizable superuser creation
- **Type Safety** with full MyPy integration
- **Code Quality** with automated linting and formatting

## 🛠 Tech Stack

- **Backend**: Django 6.0+, Django REST Framework
- **Database**: SQLite (dev), PostgreSQL/MySQL (prod)
- **Deployment**: Docker, Podman, Gunicorn, Nginx
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
cd backend

# Install dependencies and setup
task setup
```

### 2. Configure Environment
```bash
# Copy environment template
cp ../env.example .env

# Edit environment variables
# Update SECRET_KEY, database settings, etc.
```

### 3. Run Development Server
```bash
# Start development server
task dev

# Or use individual commands
task backend:migrate
task backend:runserver
```

### 4. Access Application
- **API**: http://localhost:8000/
- **Admin**: http://localhost:8080/admin/
- **Health Check**: Built-in health monitoring

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
# Create default admin user
task backend:createadmin

# Create custom admin user
task backend:createadmin -- --username admin --email admin@example.com --password secure123

# Update existing user
task backend:createadmin -- --force
```

## 📖 API Documentation

### Base URL
```
http://localhost:8080/  (production via nginx)
http://localhost:8000/  (development direct)
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

## 🧪 Development

### Available Tasks

```bash
# Backend operations
task be                    # Show backend tasks
task test                  # Run tests
task dev                   # Start development server
task migrate               # Run database migrations
task shell                 # Django shell
task lint                  # Code linting
task format                # Code formatting

# Container operations
task up                    # Start containers
task down                  # Stop containers
task logs                  # View container logs
task rebuild               # Rebuild containers

# Utilities
task setup                 # Initial development setup
task clean-all             # Clean everything
```

### Code Quality

The project uses automated code quality tools:

```bash
# Run all quality checks
task pre-commit

# Individual tools
task lint          # Ruff linting
task format        # Ruff formatting
task type-check    # MyPy type checking
```

### Testing

```bash
# Run all tests
task test

# Run with coverage
uv run pytest --cov=backend --cov-report=html

# Run specific tests
uv run pytest backend/tests/test_basic.py
```

## 🚢 Deployment

### Production Deployment

1. **Build and run containers:**
```bash
task rebuild
```

2. **Scale services:**
```bash
podman compose up -d --scale backend=3
```

3. **View logs:**
```bash
task logs
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
backend/
├── backend/              # Django project
│   ├── settings.py       # Django settings with env vars
│   ├── urls.py           # URL configuration
│   ├── wsgi.py           # WSGI application
│   ├── asgi.py           # ASGI application
│   └── management/       # Custom management commands
│       └── commands/
│           └── createadmin.py
├── tests/                # Test suite
│   ├── __init__.py
│   └── test_basic.py
├── manage.py             # Django management script
├── checkhealth.py        # Health check script
├── entrypoint.prod.sh    # Production entrypoint
├── pyproject.toml        # Python project configuration
├── pytest.ini            # Test configuration
├── ruff.toml            # Linting configuration
├── mypy.ini             # Type checking configuration
└── uv.lock              # Dependency lock file

nginx/django.conf         # Nginx configuration
docker-compose.yml        # Container orchestration
env.example              # Environment template
.gitignore              # Git ignore rules
Taskfile.yml            # Development tasks
```

## 🤝 Contributing

### Development Setup

1. Fork the repository
2. Clone your fork: `git clone <your-fork-url>`
3. Set up development environment: `task setup`
4. Create feature branch: `git checkout -b feature/your-feature`
5. Make changes and ensure tests pass
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
- Django REST Framework
- Modern Python tooling ecosystem
- Containerization best practices

---

**Built with ❤️ using Django 6.0+ and modern Python practices**
