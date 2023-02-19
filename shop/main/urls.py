from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    # path("product/<slug>", views.ProductDetailView.as_view(), name='detail'),
    path('shop/', views.ShopView.as_view(), name='shop'),
    path('product/<slug>', views.ProductDetailView.as_view(), name='detail'),
    path('shop/', views.ShopView.as_view(), name='shop'),
]