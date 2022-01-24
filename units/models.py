

from django.db import models

from store.models import User

    
class Unit(models.Model):
    type = models.CharField(max_length=100) #type of storage
    booked = models.BooleanField(default=False)
    charge = models.IntegerField() #cost per unit
    
    
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
        
    
    
class Goods(models.Model):
    storage_type  = models.CharField(max_length=100) #type of storage
    unit_no = models.ForeignKey(Unit,on_delete=models.CASCADE,related_name='store' ,null=True)
    arrival_date = models.DateField()
    departure_date = models.DateField()
    description = models.TextField(max_length=500)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='goods')
    
    def __str__(self):
        return str(self.owner)

    def add_goods(self):
        self.save()

    def remove_goods(self):
        self.delete()

