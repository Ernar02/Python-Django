from django.urls import path

from mainapp.views import index, contacts, about, products

app_name = 'mainapp'

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('products/', products, name='products'),
    path('contacts/', contacts, name='contacts'),
]