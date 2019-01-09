from django.db import models
class Product(models.Model):
    Name = models.CharField(max_length=255)
    Count = models.IntegerField()
    Price = models.IntegerField()

    