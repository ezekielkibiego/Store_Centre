from django.test import TestCase
from store.models import *
class ProfileTestClass(TestCase):  # Profile class test
    def setUp(self):
        # create a user
        user = User.objects.create(
            username="test_user", first_name="store", last_name="centre"
        )

        self.profile = Profile(
            bio="Test Bio",
            user=user,
            phone="Test Phone",
        )

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

class ClientTestClass(TestCase):
    def setUp(self):
        self.client = Client(location='Test Client')

    def test_instance(self):
        self.assertTrue(isinstance(self.client, Client))

    # def test_save_method(self):
    #     self.client.save()
    #     clients = Client.objects.all()
    #     self.assertTrue(len(clients) > 0)

    # def test_delete_method(self):
    #     self.client.save()
    #     self.client.delete_client()
    #     clients = Client.objects.all()
    #     self.assertTrue(len(clients) == 0)

class StaffTestClass(TestCase):
    def setUp(self):
        self.staff = Staff(designation='Test Staff')

    def test_instance(self):
        self.assertTrue(isinstance(self.staff, Staff))