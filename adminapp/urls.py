from django.urls import path
import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('', adminapp.index, name='index'),

    path('users/', adminapp.admin_users, name='admin_users'),
    path('users/create/', adminapp.admin_users_create, name='admin_users_create'),
    path('users/update/<int:user_id>/', adminapp.admin_users_update, name='admin_users_update'),
    path('users/delete/<int:id_del>/', adminapp.admin_users_delete, name='admin_users_delete'),

    path('categories/', adminapp.admin_categories, name='admin_categories'),
    path('categories/create/', adminapp.admin_categories_create, name='admin_categories_create'),
    path('categories/update/<int:categ_id>/', adminapp.admin_categories_update, name='admin_categories_update'),
    path('categories/delete/<int:categ_id_del>/', adminapp.admin_categories_delete, name='admin_categories_delete'),

]
