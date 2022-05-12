from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Exercise(models.Model):
    name = models.CharField(max_length=255, null=False, unique=True)
    hours = models.SmallIntegerField()
    min = models.SmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
