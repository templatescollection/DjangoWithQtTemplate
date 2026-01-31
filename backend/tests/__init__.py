import pytest
from django.conf import settings
from rest_framework.test import APIClient

if not settings.configured:
    settings.configure(
        DEBUG=True,
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": ":memory:",
            },
        },
        INSTALLED_APPS=[
            "django.contrib.auth",
            "django.contrib.contenttypes",
        ],
        SECRET_KEY="test-secret-key",  # noqa: S106
        USE_TZ=True,
    )

    import django

    django.setup()


from django.core.management import execute_from_command_line


@pytest.fixture(scope="session")
def django_db_setup() -> None:
    """Set up test database."""
    execute_from_command_line(["manage.py", "migrate", "--run-syncdb"])


@pytest.fixture
def api_client() -> APIClient:
    """Create a test client for API testing."""
    return APIClient()
