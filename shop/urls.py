from django.contrib import admin
from django.urls import path, include
from mainapp import views as mainapp_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainapp_views.index, name='main'),
    path('products/', include('mainapp.urls', namespace='products')),

    path('auth/', include('authapp.urls', namespace='auth')),

    path('baskets/', include('basketapp.urls', namespace='baskets')),

    path('admin-staff/', include('adminapp.urls', namespace='admin_staff')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)