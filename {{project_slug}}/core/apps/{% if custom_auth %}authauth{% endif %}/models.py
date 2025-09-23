from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.models import Group as DefaultGroup
from django.core.validators import RegexValidator
from django.db import models


class UserManager(BaseUserManager):
    def _validate_and_normalize_login_field(self, login_field, login_value):
        """Validate and normalize login field value"""
        if not login_value:
            raise ValueError(f"The {login_field.capitalize()} field must be set")

        if login_field == "email":
            return self.normalize_email(login_value)
        elif login_field == "phone":
            normalized = login_value.replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
            if not normalized.startswith("+"):
                normalized = "+" + normalized
            return normalized

        return login_value

    def create_user(self, login_value=None, password=None, **extra_fields):
        login_field = settings.AUTH_LOGIN_FIELD

        # If login_value passed as positional, map it to correct field
        if login_value is not None:
            extra_fields[login_field] = login_value

        # Get from extra_fields if not passed as positional
        login_value = extra_fields.get(login_field)

        # Validate and normalize
        normalized_value = self._validate_and_normalize_login_field(login_field, login_value)
        extra_fields[login_field] = normalized_value

        user = self.model(**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, login_value=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(login_value, password, **extra_fields)


class User(AbstractUser):
    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
    )

    email = models.EmailField(unique=True, blank=True, null=True)
    phone = models.CharField(validators=[phone_regex], max_length=17, unique=True, blank=True, null=True)

    username = None
    USERNAME_FIELD = settings.AUTH_LOGIN_FIELD
    REQUIRED_FIELDS = []

    objects = UserManager()

    @property
    def login_field_value(self):
        return getattr(self, settings.AUTH_LOGIN_FIELD)

    def __str__(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.login_field_value or "User"


class Group(DefaultGroup):
    """Proxy model for Group with custom methods"""

    class Meta:
        proxy = True

    def __str__(self):
        return self.name
