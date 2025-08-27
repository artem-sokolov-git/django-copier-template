from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db import IntegrityError

from core.project.settings import env

User = get_user_model()


class Command(BaseCommand):
    def _message(self, message_type: str, message_text: str) -> None:
        """Helper method for outputting styled messages."""
        style_func = getattr(self.style, message_type.upper(), None)
        if style_func:
            self.stdout.write(style_func(message_text))
        else:
            self.stdout.write(message_text)

    def handle(self, *args, **options):
        admin_login = env.str("ADMIN_LOGIN")
        admin_email = env.str("ADMIN_EMAIL")
        admin_password = env.str("ADMIN_PASSWORD")

        if all([admin_login, admin_email, admin_password]):
            try:
                User.objects.create_superuser(admin_login, admin_email, admin_password)
                self._message("success", f'Superuser "{admin_login}" created successfully')

            except IntegrityError:
                self._message("warning", f'User "{admin_login}" already exists')

            except Exception as e:
                self._message("error", f"Error creating user: {e}")
        else:
            self._message(
                "error",
                "Not all environment variables are set (ADMIN_LOGIN, ADMIN_EMAIL, ADMIN_PASSWORD)",  # noqa
            )
