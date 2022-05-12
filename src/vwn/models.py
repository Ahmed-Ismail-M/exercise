from django.db import models

# Create your models here.
class Exercise(models.Model):
    name = models.CharField(max_length=255, null=False, unique=True)
    hours = models.SmallIntegerField()
    min = models.SmallIntegerField()
    def __str__(self):
        return self.name.capitalize()

