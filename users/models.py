from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Events(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='1')
    title = models.CharField(max_length=100)
    meet_id = models.CharField(max_length=5, unique=True)
    description = models.TextField(max_length=250, default='')
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title