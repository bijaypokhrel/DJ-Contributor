from django.db import models

class Bank(models.Model):
    name = models.CharField(max_length=255)
    capital = models.DecimalField(max_digits=10, decimal_places=2)
