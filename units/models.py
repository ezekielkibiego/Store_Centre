from django.contrib.auth.models import User
from django.db import models

class Goods(models.Model):
    arrival_date = models.DateTimeField(auto_now_add=True)
    departure_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=500)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='goods')
    
    def __str__(self):
        return str(self.owner)
    
class Unit(models.Model):
    type = models.CharField(max_length=100) #type of storage
    booked = models.BooleanField(default=False)
    charge = models.IntegerField() #cost per unit
    goods = models.ForeignKey(Goods,null=True,on_delete=models.SET_NULL)
    
    
    def add_unit(self):
        self.save()
        
    def delete(self):
        self.delete()
        
    @classmethod   
    def all_units(self):
        units = Unit.objects.all()
        return units
        
    
    def __str__(self):
        return  self.type     
        
    
    