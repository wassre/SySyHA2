from django.db import models

# Create your models here.
class Item(models.Model):
    task = models.CharField(max_length=160)
    deadline = models.CharField(max_length=10)
    progress = models.CharField(max_length=5)
    complete = models.BooleanField()

    def __str__(self):
        return self.task