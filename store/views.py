from django.shortcuts import get_object_or_404, render

from .models import Product


def product_list(request):
    products = Product.products.all()
    return render(request, 'store/product_list.html', {'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    return render(request, 'store/products/single.html', {'product': product})


def category_list(request, slug):
    products = Product.products.filter(category__name=slug)
    return render(request, 'store/products/category.html', {'products': products})
