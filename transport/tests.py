from django.test import TestCase
from transport.models import *


class TransportTestCase(TestCase):
    def setUp(self):
        self.user = User(password='12345678',is_superuser=False,username='usertest',email='123@gmail.com',is_active=True, is_client=True, is_staff=False,is_verified=False,first_name='user',last_name='test')
        self.user.save()
        self.transport_request = Transport(transport_type=Transport.PICKUP,address='Ngong Road, Nairobi, Kenya',email='123@gmail.com',phone_number='0712345678',distance=3.96,is_paid=False,is_approved=True,user=self.user)
        self.transport_request.save()
    
    def tearDown(self):
        '''Clears the database after every test'''
        User.objects.all().delete()
        Transport.objects.all().delete()

    def test_save_transport_request(self):
        self.transport_request.create_request()
        requests = Transport.objects.all()
        self.assertTrue(len(requests)==1)

    def test_get_requests(self):
        self.transport_request.create_request()
        requests = Transport.get_requests()
        self.assertTrue(len(requests)==1)

    def test_find_request(self):
        self.transport_request.create_request()
        got_request= Transport.find_request(1)
        self.assertEquals(self.transport_request,got_request)
