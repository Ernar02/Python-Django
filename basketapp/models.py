from django.conf import settings
from django.db import models

from mainapp.models import Product


class Basket(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='basket',
        verbose_name='Пользователь',
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='Товар',
    )

    quantity = models.PositiveIntegerField(
        verbose_name='количество',
        default=0,
    )

    add_datetime = models.DateTimeField(
        verbose_name='время',
        auto_now_add=True,
    )

    @property
    def product_cost(self):
        return self.product.price * self.quantity

    @property
    def total_quantity(self):
        _items = Basket.objects.filter(user=self.user)
        _total_quantity = sum(list(map(lambda x: x.quantity, _items)))
        return _total_quantity

    @property
    def total_cost(self):
        _items = Basket.objects.filter(user=self.user)
        _total_cost = sum(list(map(lambda x: x.product_cost, _items)))
        return _total_cost

    def __str__(self):
        return f'Корзина для {self.user} {self.product}'

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'