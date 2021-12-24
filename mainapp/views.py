from django.shortcuts import render, get_object_or_404
from mainapp.models import ProductCategory
from mainapp.models import Product
from basketapp.models import Basket


def products(request, pk=None):
    title = 'каталог'
    links_menu = ProductCategory.objects.all()
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    basket_sum = 0
    for item in Basket.objects.all():
        basket_sum += item.quantity

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')
        product_1 = Product.objects.all()[2]
        context = {
            'title': title,
            'links_menu': links_menu,
            'product_1': product_1,
            'products': products,
            'category': category,
            'basket': basket,
            'basket_sum': basket_sum,
        }
        return render(request, 'mainapp/products.html', context=context)

    same_products = Product.objects.all()
    product_1 = Product.objects.all()[2]
    context = {
        'title': title,
        'links_menu': links_menu,
        'product_1': product_1,
        'same_products': same_products,
        'basket': basket,
        'basket_sum': basket_sum,
    }
    return render(request, 'mainapp/products.html', context=context)
