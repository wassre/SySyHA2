from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator

class Item(models.Model):
    task = models.CharField(max_length=160)
    deadline = models.DateField()
    progress = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
    )

    def __str__(self):
        return self.task
