from typing import ClassVar

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractUser):
    username: None = None  # type: ignore[assignment]
    email = models.EmailField(_('email address'), unique=True)
    patronymic = models.CharField(_('patronymic'), max_length=150, blank=True)
    USERNAME_FIELD: ClassVar[str] = 'email'  # type: ignore[misc]
    REQUIRED_FIELDS: ClassVar[list[str]] = []

    objects: ClassVar[UserManager] = UserManager()  # type: ignore[assignment]

    def __str__(self) -> str:
        return self.email
