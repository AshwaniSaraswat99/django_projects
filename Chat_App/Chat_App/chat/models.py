from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=100, unique=True)
    user_name = models.CharField(max_length=200)
    def __str__(self):
        return f"Room: {self.name} (Created by {self.user_name})"

class Chatmessage(models.Model):
    message = models.CharField(max_length=10000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=200)
            