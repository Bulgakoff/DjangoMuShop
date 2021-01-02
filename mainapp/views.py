from django.shortcuts import render
from mainapp.models import ProductCategory, Product


# Create your views here.
def index(request):
    context = {'title': 'Главная страница', }

    return render(request, 'mainapp/index.html', context)


def products(request, pk=None):
    context = {'title': 'Продукты',
               'products': Product.objects.all(),
               'categories': ProductCategory.objects.all(),
               }
    return render(request, 'mainapp/products.html', context)
