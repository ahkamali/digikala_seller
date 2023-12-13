from django.db import models


# Create your models here.
class ProductPricing(models.Model):
    product_id = models.IntegerField()
    price = models.IntegerField()
    timestamp = models.DateTimeField()



