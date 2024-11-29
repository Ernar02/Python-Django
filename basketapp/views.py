from lib2to3.fixes.fix_input import context

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse

from basketapp.models import Basket
from mainapp.models import Product
from mainapp.views import get_menu_links


@login_required
def basket(request):
    if request.user.is_authenticated:
        basket_obj = Basket.objects.filter(user=request.user)
        context = {
            'basket': basket_obj,
            'menu_links': get_menu_links(),
        }
        return render(request, 'basketapp/basket.html', context)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def basket_add(request, pk):
    product = get_object_or_404(Product, pk=pk)
    basket = Basket.objects.filter(user=request.user, product=product).first()

    if not basket:
        basket = Basket(user=request.user, product=product)

    basket.quantity += 1
    basket.save()

    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('mainapp:product', args=[pk]))

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_edit(request, pk, quantity):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        basket = Basket.objects.get(pk=pk)
        if quantity > 0:
            basket.quantity = quantity
            basket.save()
        else:
            basket.delete()

        baskets = Basket.objects.filter(user=request.user)
        context = {
            'basket': baskets,
        }
        result = render_to_string('basketapp/includes/inc_basket_list.html', context)
        return JsonResponse({'result': result})


@login_required
def basket_remove(request, pk):
    basket = get_object_or_404(Basket, pk=pk, user=request.user)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))