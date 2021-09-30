from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Customer(models.Model):
    name = models.CharField(max_length=100, null=True)
    email =models.EmailField(null=True)

    def __str__(self):
        return self.name


class Events(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=100,null=True)
    meet_id = models.CharField(max_length=5, unique=True)
    description = models.TextField(max_length=250, default='')
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

#Related Set Examples
#
# parent=Customer.objects.first()
# parent.events_set.all()