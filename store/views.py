from django.shortcuts import render, get_object_or_404
from .models import Product


def home(request):
    return render(request, 'store/base.html')


def products(request):
    products = Product.objects.all()
    return render(request, 'store/products.html', {'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    return render(request, 'store/product_detail.html', {'product': product})


def category_detail(request, slug):
    products = Product.objects.filter(category__name=slug)
    return render(request, 'store/category_detail.html', {'products': products})
