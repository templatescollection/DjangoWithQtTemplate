from typing import TypedDict, Unpack

from django.conf import settings
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandParser


class UserInfo(TypedDict):
    username: str
    email: str
    password: str
    force: bool


class Command(BaseCommand):
    help = "Creates a default admin user if it doesn't exist"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "--username",
            default="admin",
            help="Username for the admin user (default: admin)",
        )
        parser.add_argument(
            "--email",
            default="admin@example.com",
            help="Email for the admin user (default: admin@example.com)",
        )
        parser.add_argument(
            "--password",
            default="admin123",
            help="Password for the admin user (default: admin123)",
        )
        parser.add_argument(
            "--force",
            action="store_true",
            help="Force update password if user already exists",
        )

    def handle(self, **options: Unpack[UserInfo]) -> None:
        username = options["username"]
        email = options["email"]
        password = options["password"]
        force = options["force"]

        # Check if user already exists
        try:
            user = User.objects.get(username=username)
            if force:
                user.set_password(password)
                user.email = email
                user.save()
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully updated admin user "{username}"'),
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f'Admin user "{username}" already exists. '
                        "Use --force to update.",
                    ),
                )
                return
        except User.DoesNotExist:
            # Create new user
            user = User.objects.create_superuser(
                username=username,
                email=email,
                password=password,
            )
            self.stdout.write(
                self.style.SUCCESS(f'Successfully created admin user "{username}"'),
            )

        # Display login information
        self.stdout.write("\n" + "=" * 50)
        self.stdout.write("ADMIN USER CREDENTIALS:")
        self.stdout.write(f"Username: {username}")
        self.stdout.write(f"Email: {email}")
        self.stdout.write(f"Password: {password}")
        self.stdout.write("=" * 50)

        # Check if we're in development
        if getattr(settings, "ENVIRONMENT", "production") == "development":
            self.stdout.write("\n⚠️  WARNING: Using default credentials in development!")
            self.stdout.write("   Make sure to change the password in production.")
        else:
            self.stdout.write("\n✅ Production environment detected.")
            self.stdout.write("   Remember to change the default password!")
