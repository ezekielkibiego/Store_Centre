import email
from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save


class User(AbstractUser):
  
    is_client = models.BooleanField('client status',default=False)
    is_staff = models.BooleanField('staff status',default=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    last_login = models.CharField(max_length=1000,null=True)

    def save_user(self):
        self.save()
    def update_user(self):
        self.update()
    def delete_user(self):
        self.delete()

# PROFILE_TYPES = (
#     (u'CLT', 'Client'),
#     (u'STF', 'Staff'),
# )

# # used just to define the relation between User and Profile
# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     profile = models.ForeignKey('Profile',  on_delete=models.CASCADE)
#     type = models.CharField(choices=PROFILE_TYPES, max_length=16)

# # common fields reside here
class Profile(models.Model):
    verified = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',null=True)
    profile_photo = CloudinaryField("image",null=True)
    bio = models.TextField(max_length=300,null=True)
    location = models.CharField(max_length=30,null=True)
    email = models.CharField(max_length=100,null=True)
    phone = models.CharField(max_length=100,null=True)
    date = models.DateTimeField(auto_now_add=True,null=True)
    

    def __str__(self):
        return f'{self.user.username} profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(bio=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()



class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(max_length=20, null=True)
    location = models.CharField(max_length=50,null=True)
    email = models.CharField(max_length=50,null=True)
    last_login = models.CharField(max_length=1000,null=True)

    def save_client(self):
        self.save()
    def update_client(self):
        self.update()
    def delete_client(self):
        self.delete()

    def __str__(self):
        return f'{self.user}'

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(max_length=20,null=True)
    email = models.CharField(max_length=50,null=True)
    designation = models.CharField(max_length=50,null=True)
    last_login = models.CharField(max_length=1000,null=True)

    def save_staff(self):
        self.save()
    def update_staff(self):
        self.update()
    def delete_staff(self):
        self.delete()

    def __str__(self):
        return f'{self.user}'



