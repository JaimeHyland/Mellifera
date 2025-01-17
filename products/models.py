from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    materials = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()
    has_clothing_sizes = models.BooleanField(default=False, null=True, blank=True)
    husbandry_system = models.ForeignKey(
        'husbandry_system.HusbandrySystem',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1824, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    in_stock = models.BooleanField(default=True)
    current = models.BooleanField(default=True)

    def __str__(self):
        return self.name
