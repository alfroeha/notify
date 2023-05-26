from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a new user.
        """
        if not email:
            raise ValueError("The Email field must be set.")
        
        # Normalize the email address by lowercasing the domain part of it
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):
    username = models.CharField(max_length=30)
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        # Add the unique constraint to the 'username' field
        constraints = [
            models.UniqueConstraint(fields=['username'], name='unique_username'),
        ]

    def __str__(self):
        return self.username
