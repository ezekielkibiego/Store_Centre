from django.db import models
from django.contrib.auth.models import User

class Transport(models.Model):
    PICKUP='Pick-Up'
    DELIVERY = 'Delivery'
    TRANSPORT_CHOICES=(
        (PICKUP,'Pick-Up'),
        (DELIVERY,'Delivery'),
        
    )
    transport_type = models.CharField(
        max_length=10,
        choices=TRANSPORT_CHOICES,
        default=PICKUP
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='request_owner')
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, null=True)
    
    def __str__(self):
        return self.county
