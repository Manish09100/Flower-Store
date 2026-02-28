from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    old_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount = models.CharField(max_length=10, null=True, blank=True, help_text="e.g. -10%")
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name
