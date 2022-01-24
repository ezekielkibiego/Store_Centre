from django.urls import path,include
from .views import IndexView
from . import views


urlpatterns = [
    path('', IndexView, name='index'),
    path('records/', views.records, name='records'),
    path('services/', views.services, name='services'),
    path('register/',views.register, name='register'),
    path('client_register/',views.client_register.as_view(), name='client_register'),
    path('staff_register/',views.staff_register.as_view(), name='staff_register'),
    path('client_login/',views.client_login, name='client_login'),
    path('staff_login/',views.staff_login, name='staff_login'),
    path('logout/',views.logout_view, name='logout'),


    path("change_password/", views.change_password, name="change_password"),
    path("admin_login/", views.admin_login, name="admin_login"),
    # path('profile/', views.profile, name='profile'),
    # path('accounts/profile/', views.IndexView,name='index'),
    # path('update_profile/<int:id>',views.update_profile, name='update_profile'),
 
    

]