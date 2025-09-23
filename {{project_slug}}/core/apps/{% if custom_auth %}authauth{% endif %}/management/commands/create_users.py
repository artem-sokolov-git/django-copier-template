import json
from pathlib import Path

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()


class CustomCommand(BaseCommand):
    def _message(self, message_type: str, message_text: str) -> None:
        """Helper method for outputting styled messages."""
        style_func = getattr(self.style, message_type.upper(), None)
        if style_func:
            self.stdout.write(style_func(message_text))
        else:
            self.stdout.write(message_text)


class Command(CustomCommand):
    help = "Create users from users.json file (only in DEBUG mode)"

    @property
    def login_field(self):
        return settings.AUTH_LOGIN_FIELD

    @property
    def users_json(self):
        """Get path to users.json file"""
        return Path(settings.USERS_JSON_PATH)

    def _load_users_json(self, json_path: Path) -> list[dict] | None:
        """Load user data from JSON file"""
        if not json_path.exists():
            self._message("error", f"users.json file not found at {json_path}")
            return None

        try:
            users_list = json.loads(json_path.read_text(encoding="utf-8"))

            if not isinstance(users_list, list):
                self._message("error", "users.json should contain a list of users")
                return None

            return users_list

        except json.JSONDecodeError as e:
            self._message("error", f"Invalid JSON format in users.json: {e}")
            return None
        except Exception as e:
            self._message("error", f"Error reading users.json: {e}")
            return None

    def _validate_user_data(self, user_data: dict) -> tuple[bool, str | None]:
        """Validate user data"""
        if not isinstance(user_data, dict):
            return False, "Invalid user data format"

        # Check required fields
        for field in (self.login_field, "password"):
            if not user_data.get(field):
                return False, f"Missing {field}"

        # Check uniqueness for email and phone
        for field in ("email", "phone"):
            value = user_data.get(field)
            if value and User.objects.filter(**{field: value}).exists():
                return False, f'User with {field} "{value}" already exists'

        return True, None

    def _create_user(self, user_data: dict) -> bool:
        """Create user from json data"""
        try:
            login_value = user_data.get(self.login_field, "Unknown")
            is_superuser = user_data.get("is_superuser", False)

            if is_superuser:
                User.objects.create_superuser(**user_data)
                self._message("success", f'Superuser "{login_value}" created successfully')
            else:
                User.objects.create_user(**user_data)
                self._message("success", f'User "{login_value}" created successfully')

            return True

        except Exception as e:
            self._message("error", f"Error creating user {login_value}: {e}")
            return False

    def handle(self, *args, **options):
        """Create users from users.json file (only in DEBUG mode)"""
        if not settings.DEBUG:
            self._message("error", "This command can only be run in DEBUG mode")
            return

        users_data = self._load_users_json(self.users_json)

        if users_data is None:
            return

        for user_data in users_data:
            is_valid, error_msg = self._validate_user_data(user_data)

            if not is_valid:
                self._message("warning", f"Skipping user: {error_msg}")
                continue

            self._create_user(user_data)
