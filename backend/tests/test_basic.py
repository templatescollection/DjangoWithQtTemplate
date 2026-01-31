"""Basic tests for the Django project."""

from django.test import TestCase
from django.urls import reverse

REDIRECT = 302


class BasicTestCase(TestCase):
    """Basic test cases for the Django application."""

    def test_admin_url_exists(self) -> None:
        """Test that admin URL is accessible."""
        url = reverse("admin:index")
        response = self.client.get(url)
        # Should redirect to login page
        assert response.status_code == REDIRECT  # noqa: S101

    def test_health_check(self) -> None:
        """Test basic health check."""
        # This is a placeholder - add actual health check endpoint test
        assert True  # noqa: S101
