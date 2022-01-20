from django import views
from django.urls import path
from transport import views

urlpatterns=[
    path('request-transport/',views.request_transport,name='transport_request')
]