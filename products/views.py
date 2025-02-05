from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
import os
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse

# Список товарів
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

# Додавання товару


def add_product(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(request, "products/add_product.html", {"form": form, "id": id})

# Оновлення товару 
def edit_product(request, id):
    product = Product.objects.get(id=id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/edit_product.html', {'form': form})

# Видалення товару
def delete_product(request, id):
    product = Product.objects.get(pk=id)
    if product is None:
        return HttpResponse("Guitar not found")
    product.delete()
    return redirect("/")