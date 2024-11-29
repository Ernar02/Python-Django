from django.shortcuts import render, get_object_or_404, redirect
from unicodedata import category

from authapp.forms import ShopUserRegisterForm, ShopCategoryCreateForm, ShopUserEditForm, ShopUserDeleteForm, \
    ShopProductUpdateForm, ShopCategoryUpdateForm, ShopCategoryDeleteForm, ShopProductCreateForm, ShopProductDeleteForm
from authapp.models import ShopUser
from mainapp.models import Category, Product


def user_create(request):
    page_title = 'Админка | Пользователи | Создание'

    if request.method == 'POST':
        form = ShopUserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('adminapp:users')
    else:
        form = ShopUserRegisterForm()

    context = {
        'title': page_title,
        'form': form
    }

    return render(request, 'adminapp/user_create.html', context)


def users(request):
    page_title = 'Админка | Пользователи'
    user_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')

    context = {
        'title': page_title,
        'objects': user_list,
    }

    return render(request, 'adminapp/users.html', context)


def user_update(request, pk):
    page_title = 'Админка | Пользователи | Редактирование'
    user = get_object_or_404(ShopUser, pk=pk)

    if request.method == 'POST':
        form = ShopUserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('adminapp:users')
    else:
        form = ShopUserEditForm(instance=user)

    context = {
        'title': page_title,
        'form': form
    }
    return render(request, 'adminapp/users_update.html', context)




def user_delete(request, pk):
    user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        user.delete()

    return redirect('adminapp:users')



def category_create(request):
    page_title = 'Админка | Категории | Создание'

    if request.method == 'POST':
        form = ShopCategoryCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('adminapp:categories')
    else:
        form = ShopCategoryCreateForm()

    context = {
        'title': page_title,
        'form': form
    }

    return render(request, 'adminapp/category_create.html', context)


def categories(request):
    page_title = 'Админка | Категории'
    categories_list = Category.objects.all()
    context = {
        'title': page_title,
        'objects': categories_list,
    }

    return render(request, 'adminapp/categories.html', context)


def category_update(request, pk):
    page_title = 'Админка | Категории | Редактирование'
    category = get_object_or_404(Category, pk=pk)
    form = ShopCategoryUpdateForm(instance=category)

    if request.method == 'POST':
        form = ShopCategoryUpdateForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('adminapp:categories')

    context = {
        'title': page_title,
        'form': form
    }

    return render(request, 'adminapp/category_update.html', context)


def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        category.delete()
        return redirect('adminapp:categories')



def product_create(request, pk):
    page_title = 'Админка | Продукт | Создание'
    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        form = ShopProductCreateForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.category = category
            product.save()
            return redirect('adminapp:product_read', pk=category.pk)
    else:
        form = ShopProductCreateForm()

    context = {
        'title': page_title,
        'form': form,
        'category': category,
    }

    return render(request, 'adminapp/product_create.html', context)


def products(request, pk):
    page_title = 'Админка | Продукты'
    category = get_object_or_404(Category, pk=pk)
    products_list = Product.objects.filter(category=category).order_by('name')

    context = {
        'title': page_title,
        'category': category,
        'objects': products_list,
    }

    return render(request, 'adminapp/products.html', context)



def product_read(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    context = {
        'categories': categories,
        'products': products,
    }

    return render(request, 'adminapp/product_read.html', context)


def product_update(request, pk):
    page_title = 'Админка | Продукты | Редактирование'
    product = get_object_or_404(Product, pk=pk)
    category = product.category  # Получаем категорию из продукта
    form = ShopProductUpdateForm(request.POST or None, request.FILES or None, instance=product)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('adminapp:product_read', pk=category.pk)

    context = {
        'title': page_title,
        'form': form,
        'category': category,
    }

    return render(request, 'adminapp/product_update.html', context)




def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        category_pk = product.category.pk
        product.delete()
        return redirect('adminapp:product_read', pk=category_pk)


