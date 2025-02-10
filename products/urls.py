from django.urls import path
from .views import *

urlpatterns = [
    path('', product_list, name='product_list'),
    path('add/', add_product, name='add_product'),
    path('edit', edit_product, name='edit_product'),
    path('delete', delete_product, name='delete_product'),
    path("details/<int:id>", details, name='details'),
]