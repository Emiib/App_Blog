from django.db import models
from django.contrib.auth.models import User
from datetime import datetime



class Inbox(models.Model):
    title = models.CharField(max_length=40, default="Message")
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
    reciever = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reciever")
    msg = models.TextField()
    date = models.DateTimeField(default=datetime.now) #models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.msg[:50]}[...]"