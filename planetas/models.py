from django.db import models

class Planeta(models.Model):

    name = models.CharField(max_length=255)
    image = models.ImageField()
    diameter = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
