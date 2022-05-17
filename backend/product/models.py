from django.db import models
from django.contrib.postgres.fields import ArrayField

from fabrics.models import Fabric

# Create your models here.


class Currency(models.Model):
    currency = models.CharField(max_length=6)

    def __str__(self):
        return self.currency


class ProductAttribute(models.Model):
    CLOTH_SIZE = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large')
    )
    size = ArrayField(models.CharField(
        max_length=4, choices=CLOTH_SIZE), blank=True)

    color = models.CharField(max_length=20)
    fabric = models.ForeignKey(
        Fabric, on_delete=models.CASCADE, default="none", blank=True)

    def __str__(self):
        return "Size(s): " + ", ".join(self.size) + " Color: " + self.color


class Product(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    price = models.IntegerField()
    currency = models.ForeignKey(Currency,
                                 on_delete=models.CASCADE,)
    attributes = models.ForeignKey(ProductAttribute, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.FileField(upload_to="products/")

    def __str__(self):
        return self.product.name
