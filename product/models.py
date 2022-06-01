from django.db import models

STATUS = (
    (1, "available"),
    (2, "unavailable"),
)


class Product(models.Model):
    name = models.CharField(max_length=255)
    class_name = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.ImageField(null=True, blank=True)
    status = models.PositiveSmallIntegerField(choices=STATUS, default=1)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)


class Variant(models.Model):
    title = models.CharField(max_length=40)
    available_stock = models.FloatField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="variants")
