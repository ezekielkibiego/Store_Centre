from django.test import TestCase
from .models import *


# Create your tests here.
class OrderTestClass(TestCase):
    def setUp(self):
        self.new_order = Order(product_category = 'bonded_storage',payment_method = 'mpesa',shipping_cost = '1500')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_order,Order))

    def test_save_order(self):
        self.new_order.save()
        orders = Order.objects.all()
        self.assertTrue(len(orders)>0)

    def test_delete_order(self):
        self.new_order.save()
        self.new_order.delete()
        orders = Order.objects.all()
        self.assertFalse(len(orders)>0)


    # def test_update_order(self):
    #     self.new_order.save()
        
