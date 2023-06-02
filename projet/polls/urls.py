from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('index/', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('cart/', views.cart, name='cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('logout/', views.logout_view, name='logout'),
    # path('remove_from_cart/<int:item_id>/', views.cart, name='remove_from_cart'),
    path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
]