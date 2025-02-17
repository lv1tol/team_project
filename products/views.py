from django.shortcuts import render, redirect
from .models import Product, Profile
from django.http import HttpResponse
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .forms import RegisterForm

# Список товарів
def product_list(request):
    category = request.GET.get("category", "") 
    if category:
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()

    return render(request, 'products/product_list.html', {
        'products': products,
        'selected_category': category,
    })

# Деталі товару
def details(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return HttpResponse("Product not found")
    return render(request, "products/details.html", {'product': product})

# Додавання товару
@login_required
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False) 
            product.author = request.user 
            product.save()  
            return redirect('product_list') 
    else:
        form = ProductForm()

    return render(request, "products/add_product.html", {"form": form})


# Оновлення товару
@login_required 
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
@login_required
def delete_product(request, id):
    product = Product.objects.get(pk=id)
    if product is None:
        return HttpResponse("Guitar not found")
    product.delete()
    return redirect("/")

#  Мої оголошення
@login_required
def my_listings(request):
    products = Product.objects.filter(author=request.user)
    return render(request, 'products/my_listings.html', {'products': products})

# Реєстрація
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            avatar = form.cleaned_data.get('avatar')
            Profile.objects.create(user=user, avatar=avatar)
            login(request, user)
            return redirect('product_list')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile_view(request):
    return render(request, 'profile/profile.html', {'user': request.user})

def logout_view(request):
    logout(request)
    return redirect('login')