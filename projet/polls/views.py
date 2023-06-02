from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Product
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from .models import Order, OrderItem
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import get_object_or_404, redirect

def logout_view(request):
    logout(request)
    return redirect('index')

def index(request):  
    products = Product.objects.all()
    return render(request, 'Index/index.html', {'products': products})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirige vers la page de connexion après l'inscription
    else:
        form = UserCreationForm()
    return render(request, 'registration/registration.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')  # Redirige vers la page d'accueil après la connexion
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

@login_required
def cart(request):
    user = request.user
    order = Order.objects.filter(user=user).last()
    order_items = OrderItem.objects.filter(order=order)

    total_amount = 0
    for item in order_items:
        total_amount += item.quantity * item.product.price

    context = {
        'order_items': order_items,
        'total_amount': total_amount,
    }

    return render(request, 'Cart/cart.html', context)

def add_to_cart(request, product_id):
    # Vérifier si l'utilisateur est connecté
    if request.user.is_authenticated:
        # Récupérer le produit à partir de l'ID
        product = get_object_or_404(Product, pk=product_id)

        # Récupérer ou créer la commande de l'utilisateur
        order, created = Order.objects.get_or_create(user=request.user)

        # Vérifier si le produit est déjà dans le panier
        order_item, item_created = OrderItem.objects.get_or_create(order=order, product=product)

        # Récupérer la quantité soumise dans le formulaire
        quantity = int(request.POST.get('quantity', 1))

        # Mettre à jour la quantité du produit dans le panier
        if not item_created:
            order_item.quantity += quantity
            order_item.save()

        # Rediriger vers la page d'accueil (index)
        return redirect('index')
    else:
        return redirect('login')


def remove_from_cart(request, item_id):
    if request.user.is_authenticated:
        try:
            order_item = OrderItem.objects.get(id=item_id)
            quantity = int(request.POST.get('quantity', 1))
            if quantity >= order_item.quantity:
                order_item.delete()
            else:
                order_item.quantity -= quantity
                order_item.save()
            
            return redirect('cart')
        except OrderItem.DoesNotExist:
            pass
    
    return redirect('index') 

