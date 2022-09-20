from django.db import models


class ReleaseDecade(models.Model):
    release_decade = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.release_decade


class Manufacturer(models.Model):
    manufacturer = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.manufacturer


class Cpu(models.Model):
    cpu = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.cpu


class Product(models.Model):
    release_decade = models.ForeignKey(
        "ReleaseDecade", null=True, blank=True, on_delete=models.SET_NULL
    )
    manufacturer = models.ForeignKey(
        "Manufacturer", null=True, blank=True, on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    cpu = models.ForeignKey(
        "CPU", null=True, blank=True, on_delete=models.SET_NULL
    )
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    release_year = models.IntegerField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
