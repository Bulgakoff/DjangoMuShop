from django.shortcuts import HttpResponseRedirect, get_object_or_404
from mainapp.models import Product
from basketapp.models import Basket
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import JsonResponse


# (user_passes_test(lambda u: u.is_authenticated))
@login_required
def basket_add(request, id_product=None):
    product = get_object_or_404(Product, id=id_product)
    baskets = Basket.objects.filter(user=request.user, product=product)
    if not baskets.exists():
        basket = Basket(user=request.user, product=product)
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    # return render(request, 'authapp/profile.html')


@login_required
def basket_remove(request, id=None):
    basket = Basket.objects.get(id=id)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    # return render(request, 'authapp/profile.html')


@login_required
def basket_edit(request, id, quantity):
    print(request)
    if request.is_ajax():
        quantity = int(quantity)
        basket = Basket.objects.get(id=int(id))
        if quantity > 0:
            basket.quantity = quantity
            basket.save()
        else:
            basket.delete()
        baskets = Basket.objects.filter(user=request.user)
        context = {
            'baskets': baskets,
        }
        result = render_to_string('basketapp/basket.html', context)
        return JsonResponse({'result': result})
