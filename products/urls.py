from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from .views import register

urlpatterns = [
    path('', product_list, name='product_list'),
    path('add/', add_product, name='add_product'),
    path('edit/<int:id>/', edit_product, name='edit_product'),
    path('delete/<int:id>/', delete_product, name='delete_product'),
    path("details/<int:id>", details, name='details'),
    path('my_listings/', my_listings, name='my_listings'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/register/', register, name='register'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='product_list'), name='logout'),

]