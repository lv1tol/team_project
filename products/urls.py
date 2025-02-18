from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from .views import register
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', product_list, name='product_list'),
    path('add', add_product, name='add_product'),
    path('edit/<int:id>/', edit_product, name='edit_product'),
    path('delete/<int:id>/', delete_product, name='delete_product'),
    path("details/<int:id>", details, name='details'),
    path('my_listings', my_listings, name='my_listings'),
    path('add_to_favorites/<int:id>', add_to_favorites, name='add_to_favorites'),
    path('my_favorites', my_favorites, name='my_favorites'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html', next_page='product_list'), name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)