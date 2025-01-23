from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from django.utils.timezone import now


class PreOrder(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='pre_orders'
        )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='pre_orders')
    quantity = models.PositiveIntegerField()
    date_preordered = models.DateTimeField(default=now)

    current = models.BooleanField(default=True)


    def __str__(self):
        return f"Pre-order: {self.product.name} pre-ordered by {self.user.username}"

    class Meta:
        verbose_name = "pre-order"
        verbose_name_plural = "pre-orders"
