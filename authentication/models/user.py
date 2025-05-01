from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models

from authentication.exceptions import EmailRequired, FullNameRequired


class UserManager(BaseUserManager):
    def create_user(self, email, full_name, password=None):
        if not email:
            raise EmailRequired()
        if not full_name:
            raise FullNameRequired()

        user = self.model(email=self.normalize_email(email), full_name=full_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, password=None):
        user = self.create_user(email, full_name, password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()

    email = models.EmailField(unique=True, null=False, blank=False, max_length=255)
    full_name = models.CharField(max_length=100, null=False, blank=False)
    user_tier = models.CharField(max_length=100, default="normal")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["full_name"]

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    class Meta:
        db_table = "user"
        verbose_name = "User"
        verbose_name_plural = "Users"
