from django.db import models

# Create your models here.
class Order(models.Model):
    product_category = models.CharField(max_length=20)
    payment_method = models.CharField(max_length=50)
    shipping_cost = models.CharField(max_length=50)

    def save_order(self):
        self.save()
    def update_order(self):
        self.update()
    def delete_order(self):
        self.delete()

    def __str__(self):
        return f'{self.user}'