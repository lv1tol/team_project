from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from products import views


urlpatterns = [
    path('', views.product_list),
    path('admin/', admin.site.urls),
    path('edit/<int:id>', views.edit_product),
    path('delete/<int:id>', views.delete_product),
    path('add', views.add_product),
    path("details/<int:id>", views.details, name='details'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
