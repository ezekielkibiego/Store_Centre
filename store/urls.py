from django.urls import path
from .views import IndexView
from . import views

urlpatterns = [
    path('', IndexView, name='index'),
    path("profile/", views.profile, name="profile"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),




    path("client_registration/", views.client_registration, name="client_registration"),
    path("change_password/", views.change_password, name="change_password"),
    path("client_login/", views.client_login, name="client_login"),
    path("admin_login/", views.admin_login, name="admin_login"),
    path("logout/", views.Logout, name="logout"),
]