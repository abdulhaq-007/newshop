from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.base import View
from . models import Product
# Create your views here.

class HomePageView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        
        popular_products = Product.objects.filter(top=True)
        discount_products = Product.objects.filter(discount__gte=0)
        
        data = {
            "popular_products":popular_products,
            "discount_products":discount_products
        }
        return render(request, 'index.html', context=data)        

class ShopView(TemplateView):
    template_name = 'shop.html'


class ProductDetailView(DetailView):
    template_name = "shop-single.html"
    model = Product
