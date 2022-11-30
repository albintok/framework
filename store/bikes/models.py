from django.db import models

# Create your models here.

class Vechicles(models.Model):
    name=models.CharField(max_length=20)
    colour=models.CharField(max_length=20)
    cc=models.PositiveIntegerField()
    price=models.PositiveIntegerField()
    brand=models.CharField(max_length=20)

    def __str__(self):
        return self.name