from email.policy import default
from django.db import models

from django.contrib.auth.models import User

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/avatardefault.png', null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.user.username}"