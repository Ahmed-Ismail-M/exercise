from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Exercise(models.Model):
    name = models.CharField(max_length=255, null=False)
    hours = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(24)])
    min = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(60)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
