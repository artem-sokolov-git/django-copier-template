import re
from pathlib import Path

from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand


class CustomCommand(BaseCommand):
    def _message(self, message_type: str, message_text: str) -> None:
        """Helper method for outputting styled messages."""
        style_func = getattr(self.style, message_type.upper(), None)
        if style_func:
            self.stdout.write(style_func(message_text))
        else:
            self.stdout.write(message_text)


class Command(CustomCommand):
    help = "Create Django app with proper structure"

    def _create_django_app(self, base_dir: Path, app_name: str) -> Path:
        """Create django app and return directory path."""
        apps_dir = base_dir / "core" / "apps"
        app_dir = apps_dir / app_name

        apps_dir.mkdir(parents=True, exist_ok=True)

        if app_dir.exists():
            raise FileExistsError(f"App directory {app_dir} already exists")

        app_dir.mkdir(parents=False, exist_ok=False)
        call_command("startapp", app_name, str(app_dir))

        return app_dir

    def _update_django_app_config(self, app_dir: Path, app_name: str) -> None:
        """Update app's apps.py with correct app name."""
        apps_file = app_dir / "apps.py"
        if apps_file.exists():
            content = apps_file.read_text(encoding="utf-8")
            content = content.replace(f"name = '{app_name}'", f"name = 'core.apps.{app_name}'")
            apps_file.write_text(content, encoding="utf-8")

    def _add_to_local_apps(self, base_dir: Path, app_name: str) -> bool:
        """Add app to LOCAL_APPS in settings/base.py. Returns True if added."""
        settings_file = base_dir / "core" / "project" / "settings" / "base.py"
        if not settings_file.exists():
            return False

        content = settings_file.read_text(encoding="utf-8")
        app_config = f"core.apps.{app_name}"

        if app_config in content:
            return False

        pattern = r"(LOCAL_APPS = \[.*?)(\n])"
        replacement = rf'\1\n    "{app_config}",\2'
        updated_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

        if updated_content != content:
            settings_file.write_text(updated_content, encoding="utf-8")
            return True
        return False

    def add_arguments(self, parser):
        parser.add_argument("app_name", type=str, help="Name of the app")

    def handle(self, *args, **options):
        app_name = options["app_name"]
        base_dir = Path(settings.BASE_DIR)

        try:
            app_dir = self._create_django_app(base_dir, app_name)

            self._update_django_app_config(app_dir, app_name)

            if self._add_to_local_apps(base_dir, app_name):
                self._message("success", f'Added "core.apps.{app_name}" to LOCAL_APPS')

            self._message("success", f'App "{app_name}" created at {app_dir}')

        except FileExistsError:
            return
