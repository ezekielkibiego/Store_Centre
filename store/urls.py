from django.urls import path,include
from .views import IndexView
from . import views


urlpatterns = [
    path('', IndexView, name='index'),
    path('records/', views.records, name='records'),
    path('services/', views.services, name='services'),
    path('goods/checkout/<records_id>/',views.checkout_booking,name='checkout'),
    path('checkout-goods/<int:goods_id>/',views.checkout_goods,name='checkout_goods'),
    path('register/',views.register, name='register'),
    path('client_register/',views.client_register.as_view(), name='client_register'),
    path('staff_register/',views.staff_register.as_view(), name='staff_register'),
    path('client_login/',views.client_login, name='client_login'),
    path('staff_login/',views.staff_login, name='staff_login'),
    path('logout/',views.logout_view, name='logout'),
    path("change_password/", views.change_password, name="change_password"),
    path("admin_login/", views.admin_login, name="admin_login"),
    # path('client_profile/', views.client_profile, name='client_profile'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('profile/', views.profile, name='profile'),
    # path('staff_profile/', views.staff_profile, name='staff_profile'),
    # path('update_staff_profile/',views.update_staff_profile, name='update_staff_profile'),
    path('update_profile/<int:id>',views.update_profile, name='update_profile'),
    # path('accounts/profile/', views.IndexView,name='index'),
    # path('update_client_profile/',views.update_client_profile, name='update_client_profile'),
    path('social-auth/',include('social_django.urls',namespace='social')),
    path('api/store/', views.Storelist.as_view()),
    path('news/', views.blog, name='blog')
    
    

]
handler404 = "store.views.page_not_found_view"