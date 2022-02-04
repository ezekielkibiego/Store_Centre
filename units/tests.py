
from django.test import TestCase
from . models import *
from store.models import User

# Create your tests here.

class StorageTestClass(TestCase):
    
    def setUp(self):
        self.new_store = Storage(type = 'Normal_storage',charge =100,no_units = 10,available_units=10)
       
    def test_instance(self):
        self.assertTrue(isinstance(self.new_store,Storage)) 
        
    def test_add_storage(self):
        self.new_store.add_storage()
        stores = Storage.objects.all()
        self.assertTrue(len(stores)>0)
        
    def test_remove_storage(self):
        self.new_store.add_storage()
        self.new_store.remove_storage()
        stores = Storage.objects.all()
        self.assertTrue(len(stores)==0)

    def test_all_storages(self):
        self.new_store.add_storage()
        storages = Storage.all_storages()
        self.assertIsNotNone(storages)


    def test_storage_type(self):
        self.new_store.add_storage()
        storages = Storage.storage_type('Normal_storage')
        self.assertIsNotNone(storages)
        not_existing_storages = Storage.storage_type('cool_storage')
        self.assertIsNone(not_existing_storages)

    def test_units_available(self):
        self.new_store.add_storage()
        units = Storage.units_available('Normal_storage')
        self.assertTrue(units==10)
        


class GoodsTestClass(TestCase):
    
    def setUp(self):
        self.new_user = User(username= 'Tim', first_name = 'timo', last_name ='Cornor')
        self.new_store = Storage(type = 'Normal_storage',charge =100,no_units = 10,available_units=10)
        self.new_goods = Goods(storage_type =self.new_store,no_of_units=5,arrival_date='2022-02-02',departure_date='2022-02-02',description ='Black box',owner = self.new_user)   
     
    def test_instance(self):
        self.assertTrue(isinstance(self.new_goods,Goods)) 
        
#     def test_add_goods(self):
#         self.new_store.add_storage()
#         self.new_user.save_user()
#         self.new_goods.add_goods()
#         stores = Goods.objects.all()
#         self.assertTrue(len(stores)>0)
        
        
#     def test_remove_goods(self):
#         self.new_store.add_storage()
#         self.new_user.save_user()
#         self.new_goods.add_goods()
#         stores = Goods.objects.all()
#         self.assertTrue(len(stores)>0)
#         self.new_goods.remove_goods()
#         stores = Goods.objects.all()
#         self.assertTrue(len(stores)==0)
        
    # def test_owner_goods(self):
    #     self.new_store.add_storage()
    #     self.new_user.save_user()
    #     self.new_goods.add_goods()
    #     goods = Goods.owner_goods(self,self.new_user)
    #     self.assertIsNotNone(goods)
        