from django.db import models

from store.models import User

class Storage(models.Model):
    type = models.CharField(max_length=100) #type of storage
    charge = models.IntegerField() #cost per unit
    no_units = models.IntegerField(default=0) #total number of units in a storage type
    available_units = models.IntegerField(default=0) # remaining units 

    def __str__(self):
        return self.type

    def add_storage(self):
        self.save()
        
    def delete(self):
        self.delete()
    # def __repr__(self):
    #     return '{}with{}unitscharging{}'.format(self.type,self.no_units,self.charge)

    
# class Unit(models.Model):
#     type = models.ForeignKey(Storage,on_delete=models.CASCADE,related_name='units') #type of storage
#     booked = models.BooleanField(default=False)
    

    
    
#     def add_unit(self):
#         self.save()
        
#     def delete(self):
#         self.delete()
        
#     @classmethod   
#     def all_units(self):
#         units = Unit.objects.all()
#         return units
        
    
#     def __str__(self):
#         return  self.type     
        
    
    
class Goods(models.Model):
    storage_type  = models.ForeignKey(Storage,on_delete=models.CASCADE,related_name='units') #type of storage
    no_of_units = models.IntegerField(null=True)
    arrival_date = models.DateField()
    departure_date = models.DateField()
    description = models.TextField(max_length=500)
    total_cost = models.IntegerField(null=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='goods')
    
    def __str__(self):
        return str(self.owner)

    def add_goods(self):
        self.save()

    def remove_goods(self):
        self.delete()

