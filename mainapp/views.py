from django.shortcuts import render
from mainapp.models import ProductCategory, Product
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger
from django.contrib.auth.decorators import user_passes_test
from django.views.generic.list import ListView
from authapp.models import User

# Create your views here.
@user_passes_test(lambda user: user.is_superuser)
def index(request):
    context = {'title': 'Главная страница', }

    return render(request, 'mainapp/index.html', context)

# class UserListView(ListView):
#     model = User


@user_passes_test(lambda user: user.is_superuser)
def products(request, category_id=None, page=1):
    if category_id:
        products = Product.objects.filter(category_id=category_id).order_by('price')
        context = {'title': 'Продукты',
                   'categories': ProductCategory.objects.all(),
                   'products': products,
                   }
    else:
        products = Product.objects.all().order_by('price')
        context = {'title': 'Продукты',
                   'products': products,
                   'categories': ProductCategory.objects.all(),
                   }
    paginator = Paginator(products, 3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    context.update({'products': products_paginator})

    return render(request, 'mainapp/products.html', context)
