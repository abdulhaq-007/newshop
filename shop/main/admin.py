from django.contrib import admin
from .models import Category, Color, Product, Contact
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id","name")
    prepopulated_fields = {"slug":("name",)}

    
admin.site.register(Color)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "category", "discount")
    list_filter = ("category", "top")
    search_fields = ("name", "description")
    prepopulated_fields = {"slug":("name",)}

admin.site.register(Contact)