from django import views
from django.urls import path, include
from transport import views

urlpatterns=[
    path('request-transport/',views.request_transport,name='request_transport'),
    path('request-summary/',views.request_summary,name='request_summary'),
    path('transport-summaries/',views.summaries,name='transport_summaries'),
    path('payment/',views.payment,name='payment'),
    path('access/token', views.getAccessToken, name='get_mpesa_access_token'),

]