from django.urls import path
import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('', adminapp.index, name='index'),

    path('users/', adminapp.UserListView.as_view(), name='admin_users'),
    path('users/create/', adminapp.UserCreateView.as_view(), name='admin_users_create'),
    path('users/update/<int:pk>/', adminapp.UserUpdateView.as_view(), name='admin_users_update'),
    path('users/delete/<int:pk>/', adminapp.UserDeleteView.as_view(), name='admin_users_delete'),

    path('categories/', adminapp.CategoriesListView.as_view(), name='admin_categories'),
    path('categories/create/', adminapp.CategoriesCreateView.as_view(), name='admin_categories_create'),
    path('categories/update/<int:pk>/', adminapp.CategoriesUpdateView.as_view(), name='admin_categories_update'),
    path('categories/delete/<int:pk>/', adminapp.CategoriesDeleteView.as_view(), name='admin_categories_delete'),

    path('products/', adminapp.admin_products, name='admin_products'),
    path('products/create/', adminapp.admin_products_create, name='admin_products_create'),
    path('products/update/<int:prod_id>/', adminapp.admin_products_update, name='admin_products_update'),
    path('products/delete/<int:prod_id_del>/', adminapp.admin_products_delete, name='admin_products_delete'),
]
