
from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name = 'dashboard'),
    path('user', views.user, name = 'user'),
    path('account/' , views.accountSetting, name = 'setting'),

    
    path('products',views.product, name = 'products'),
    path('customer/<str:pk>', views.customer, name = 'customer'),

    path('create_order/', views.create_order, name = 'create_order'),
    path('update_order/<str:pk>/', views.update_order, name = 'update_order'),
    path('delete_order/<str:pk>/', views.delete_order, name = 'delete_order'),
   
    path('register', views.register, name = 'register'),
    path('login', views.login, name = 'login'),
    path('logout', views.logout, name = 'logout'),
]
