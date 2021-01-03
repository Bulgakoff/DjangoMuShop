from django.db import models
from authapp.models import User
from mainapp.models import Product, ProductCategory


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина для пользователя {self.user.username}| продукт {self.product.name}'

    def sum_product(self):
        return self.quantity * self.product.price

    def total_quantity(self):
        baskets = Basket.objects.filter(user=self.user)
        return sum(basket.quantity for basket in baskets)

    def total_summa(self):
        baskets = Basket.objects.filter(user=self.user)
        return sum(basket.sum_product() for basket in baskets)
