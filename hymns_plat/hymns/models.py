from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
    )

class Hymn(models.Model):
    title = models.CharField(max_length=255)
    notes = models.TextField(blank=True)
    audio = models.FileField(upload_to='audios/')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hymns')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

