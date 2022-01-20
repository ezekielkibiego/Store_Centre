from django.db import models
from django.contrib.auth.models import User
from units.models import Goods

class Transport(models.Model):
    PICKUP='Pick-Up'
    DELIVERY = 'Delivery'
    TRANSPORT_CHOICES=(
        (PICKUP,'Pick-Up'),
        (DELIVERY,'Delivery'),
        
    )
    transport_type = models.CharField(
        max_length=7,
        choices=TRANSPORT_CHOICES,
        default=PICKUP
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='request_owner')
    county =models.CharField(max_length=50)
    town = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    goods = models.ForeignKey(Goods,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.county