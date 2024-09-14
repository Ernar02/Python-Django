from django.urls import path

from mainapp.views import index, contacts, about, products

urlpatterns = [
    path('', index),
    path('contacts/', contacts),
    path('about/', about),
    path('products/', products),
]
