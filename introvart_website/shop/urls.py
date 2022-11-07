from django.urls import path
from . import views

#app_name = "shop"

urlpatterns = [
    path('home', views.home, name = 'home'),
    path('register', views.register, name = 'register'),
    path('login', views.login_page, name = 'login'),
    path('logout', views.logout_page, name = 'logout'),
    path('cart', views.cart_page, name = 'cart'),
    path('remove_cart/<str:cid>', views.remove_cart, name = 'remove_cart'),
    path('fav', views.fav_page, name = 'fav'),
    path('favviewpage', views.favviewpage, name = 'favviewpage'),
    path('remove_fav/<str:fid>', views.remove_fav, name = 'remove_fav'),
    path('collections', views.collections, name = 'collections'),
    path('collections/<str:name>', views.collectionsview, name = 'collections'),
    path('collections/<str:cname>/<str:pname>', views.product_details, name = 'product_details'),
    path('addtocart', views.add_to_cart, name = 'addtocart'),
    path('about', views.about, name = 'about'),
    path('contact', views.contact, name = 'contact'),
    path('thank_you', views.thank_you, name = 'thank_you'),
    path('terms_cond', views.terms_cond, name = 'terms_cond'),
    path('confid', views.confid, name = 'confid'),
    path('delivery', views.delivery, name = 'delivery')
]