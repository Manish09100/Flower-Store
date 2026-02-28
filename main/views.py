from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm

def index(request):
    products = Product.objects.all()
    return render(request, 'main/index.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm()
    return render(request, 'main/add_product.html', {'form': form})

def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('index')
