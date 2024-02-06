from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="products")
    description = models.TextField()
    price = models.FloatField()

    class Meta:
        db_table = 'product_product'
        verbose_name = 'product'
        verbose_name_plural = 'products'
        ordering = ('-id',)

    def __str__(self):
        return self.name
    

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_author'
        verbose_name = 'author'
        verbose_name_plural = 'author'
        ordering = ('-id',)

    def __str__(self):
        return self.user.username