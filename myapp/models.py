from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    count = models.IntegerField()
    add_date = models.DateField()
    original_price = models.FloatField()
    benefits = models.FloatField()
    info = models.TextField(null=True)

    def __str__(self) -> str:
        return f"{self.name}"
        