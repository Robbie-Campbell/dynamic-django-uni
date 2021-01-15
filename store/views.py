from django.shortcuts import render
from .models import Product

# Create your views here.
def home (request):
    return render(request, 'store/base.html')

def products (request):
    products = Product.objects.all()
    return render(request, 'store/products.html', {'products': products})