from django.urls import path

from mainapp.views import index, contacts, about, products, product

app_name = 'mainapp'

urlpatterns = [
    path('', index, name='index'),
    path('category/<int:pk>/', products, name='category'),
    path('products/', products, name='products'),
    path('products/<int:pk>/', product, name='product'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('category/<int:pk>/page/<int:page>/', products, name='page'),
]