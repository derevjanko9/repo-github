from django.shortcuts import render
from mainapp.models import ProductCategory
from mainapp.models import Product


def products(request):
    title = 'каталог'
    links_menu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': ProductCategory.objects.all()[0].name},
        {'href': 'products_office', 'name': ProductCategory.objects.all()[1].name},
        {'href': 'products_modern', 'name': ProductCategory.objects.all()[2].name},
        {'href': 'products_classic', 'name': ProductCategory.objects.all()[3].name},
    ]
    product_1 = Product.objects.all()[2]
    context = {
        'title': title,
        'links_menu': links_menu,
        'product_1': product_1,
    }
    return render(request, 'mainapp/products.html', context=context)
