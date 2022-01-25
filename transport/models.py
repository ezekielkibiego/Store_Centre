from django.db import models
from store.models import User

class Transport(models.Model):
    PICKUP='Pick-Up'
    DELIVERY = 'Delivery'
    TRANSPORT_CHOICES=(
        (PICKUP,'Pick-Up'),
        (DELIVERY,'Delivery'),
        
    )
    transport_type = models.CharField(
        max_length=50,
        choices=TRANSPORT_CHOICES,
        default=PICKUP
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='request_owner')
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, null=True)
    distance = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    price = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    is_paid = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.transport_type
