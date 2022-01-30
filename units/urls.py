from django.urls import path
from . import views

urlpatterns = [
    path('<storage_type>',views.display_units,name='units'),
    path('',views.dashboard,name='dashboard'),
    path('book/',views.book_unit,name='book'),
   
]