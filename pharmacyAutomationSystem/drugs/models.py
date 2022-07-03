from django.db import models

class drug(models.Model):
    name = models.CharField(max_length=50, verbose_name = "product name")
    price = models.PositiveIntegerField(verbose_name="product price")
    stock = models.PositiveIntegerField(verbose_name="product stock")
    quantity = models.PositiveIntegerField(verbose_name="product quantity")
    
    def __str__(self) :
        return self.name