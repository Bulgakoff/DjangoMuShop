from django.shortcuts import render, HttpResponseRedirect, reverse
from authapp.models import User
from mainapp.models import ProductCategory, Product
from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm, CategoriesAdminCreateForm, \
    CategoriesAdminUpdateForm, ProductsAdminCreateForm, ProductsAdminUpdateForm
from django.contrib.auth.decorators import user_passes_test


# Create your views here.
@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'adminapp/index.html')


# ======================users===============================
@user_passes_test(lambda u: u.is_superuser)
def admin_users(request):
    context = {
        'users': User.objects.all(),
    }
    return render(request, 'adminapp/admin-users-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_users'))
        else:
            return HttpResponseRedirect(reverse('admin_staff:admin_users'))
    form = UserAdminRegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'adminapp/admin-users-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_users_update(request, user_id):
    # U - Update
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        form = UserAdminProfileForm(data=request.POST, files=request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_users'))
    else:
        form = UserAdminProfileForm(instance=user)

    context = {'form': form, 'user': user}
    return render(request, 'adminapp/admin-users-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_users_delete(request, id_del=None):
    user = User.objects.get(id=id_del)
    user.is_active = False
    user.save()

    return HttpResponseRedirect(reverse('admin_staff:admin_users'))


# =======================categories======================================

def admin_categories(request):
    context = {
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'adminapp/admin-category-read.html', context)


def admin_categories_create(request):
    if request.method == 'POST':
        form = CategoriesAdminCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_categories'))
        else:
            return HttpResponseRedirect(reverse('admin_staff:admin_categories'))
    form = CategoriesAdminCreateForm()
    context = {
        'form': form,
    }
    return render(request, 'adminapp/admin-category-create.html', context)


def admin_categories_update(request, categ_id):
    category = ProductCategory.objects.get(id=categ_id)
    if request.method == 'POST':
        form = CategoriesAdminUpdateForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_categories'))
        else:
            return HttpResponseRedirect(reverse('admin_staff:admin_categories'))
    form = CategoriesAdminUpdateForm(instance=category)
    context = {
        'form': form,
        'category': category,
    }

    return render(request, 'adminapp/admin-category-update-delete.html', context)


def admin_categories_delete(request, categ_id_del):
    print(f'--------------------------------------------------{categ_id_del}')
    category = ProductCategory.objects.get(id=categ_id_del)
    print(f'-------------------------------------------------->{category.is_active}')
    category.is_active = False
    category.save()

    return HttpResponseRedirect(reverse('admin_staff:admin_categories'))


# ===================products==============================

def admin_products(request):
    context = {
        'products': Product.objects.all(),
    }
    return render(request, 'adminapp/admin-products-read.html', context)


def admin_products_create(request):
    if request.method == 'POST':
        form = ProductsAdminCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_products'))
        else:
            return HttpResponseRedirect(reverse('admin_staff:admin_products'))
    form = ProductsAdminCreateForm()
    context = {
        'form': form,
    }
    return render(request, 'adminapp/admin-products-create.html', context)


def admin_products_update(request, prod_id):
    product = Product.objects.get(id=prod_id)
    if request.method == 'POST':
        form = ProductsAdminUpdateForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_products'))
        else:
            return HttpResponseRedirect(reverse('admin_staff:admin_products'))
    form = ProductsAdminUpdateForm(instance=product)
    context = {
        'form': form,
        'product': product,
    }
    return render(request, 'adminapp/admin-products-update-delete.html', context)
