from django.db import models
from django.urls import reverse


class ProductType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    name = models.CharField(max_length=255)
    product_type = models.ForeignKey(
        ProductType,
        on_delete=models.CASCADE,
        related_name='products'
    )
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=100000)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name}"

    # def get_absolute_url(self):
    #     return reverse("merchandisestore:merchandisestore-detail", kwargs={"id": self.id})
