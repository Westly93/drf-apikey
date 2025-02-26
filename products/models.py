from django.db import models

# Create your models here.
class Product(models.Model):
    name= models.CharField(max_length=255, null=False, blank=False)
    price= models.DecimalField(max_digits=6, decimal_places=2)
    in_stock= models.BooleanField()


    def __str__(self):
        return self.name