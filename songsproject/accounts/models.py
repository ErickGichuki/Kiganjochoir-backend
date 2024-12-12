from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, default='trainer')

    groups = models.ManyToManyField(
        Group,
        related_name='customer_set',
        blank=True,
        help_text='The groups the user belongs to',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customer_set',
        blank=True,
        help_text='Specific permissions for this user',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username
