from django import views
from django.urls import path
from transport import views

urlpatterns=[
    path('request-transport/',views.request_transport,name='request_transport'),
    path('request-summary/',views.request_summary,name='request_summary')

]