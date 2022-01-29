from django.contrib import admin
from .models import Client,Staff,User,Profile

admin.site.register(User)
admin.site.register(Client)
admin.site.register(Staff)
admin.site.register(Profile)