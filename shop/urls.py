
from django.contrib import admin
from django.urls import path
from mainapp import views as mainapp_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainapp_views.index),
    path('products/', mainapp_views.products),
]
