from django.shortcuts import render, get_object_or_404

from mainapp.models import Product, Category


def get_menu_links(current='mainapp:index'):
    return [
        {'href': 'mainapp:index', 'name': 'Главная', 'active': current},
        {'href': 'mainapp:products', 'name': 'Продукты', 'active': current},
        {'href': 'mainapp:about', 'name': 'О&nbsp;нас', 'active': current},
        {'href': 'mainapp:contacts', 'name': 'Контакты', 'active': current},
    ]

def index(request):
    title = 'главная'

    featured_products = Product.objects.all()

    context = {
        'title': title,
        'featured_products': featured_products,
        'menu_links': get_menu_links(),
    }

    return render(request, 'index.html', context)


def products(request, pk=None):
    title = 'товары'

    if pk:
        category = get_object_or_404(Category, pk=pk)
        products_all = Product.objects.filter(category__pk=pk)
    else:
        products_all = Product.objects.all()  # [:2]
        category = {'name': 'все'}

    categories = Category.objects.all()

    context = {
        'title': title,
        'products': products_all,
        'menu_links': get_menu_links('mainapp:products'),
        'categories': categories,
        'category': category,
    }
    return render(request, 'products.html', context)


def product(request, pk):
    title = 'Продукт'
    prod = Product.objects.get(pk=pk)
    same_products = Product.objects.exclude(pk=pk)

    context = {
        'title': title,
        'product': prod,
        'same_products': same_products,
        'menu_links': get_menu_links('mainapp:products'),
    }
    return render(request, 'product.html', context)


def about(request):
    title = 'о нас'
    context = {
        'title': title,
        'menu_links': get_menu_links('mainapp:about'),
    }
    return render(request, 'about.html', context)


def contacts(request):
    title = 'контакты'
    context = {
        'title': title,
        'menu_links': get_menu_links('mainapp:contacts'),
    }
    return render(request, 'contacts.html', context)