from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField("Kategoriya", max_length=150)
    slug = models.SlugField(max_length=150)
    image = models.ImageField
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return str(self.name)

class Color(models.Model):
    name = models.CharField("Tovar rangi", max_length=150)
    
    def __str__(self):
        return str(self.name)        

class Product(models.Model):
    name = models.CharField('Tovar nomi', max_length=150)
    slug = models.SlugField(max_length=150)
    image = models.ImageField(upload_to='product_images/',)
    category = models.ForeignKey(
        Category, 
        on_delete=models.PROTECT,
        related_name='products')
    color = models.ForeignKey(
        Color, 
        on_delete=models.PROTECT,
        related_name='color_products')
    price = models.PositiveIntegerField(default=0)
    discount = models.PositiveIntegerField("Chegirma nechi foyiz bolsin?",default=0)
    addedd =models.DateTimeField(auto_now_add=True)
    top = models.BooleanField(default=False)
    description = models.TextField()

    def get_discount_price(self):
        price = self.price
        if self.discount:            
            p = self.discount * self.price // 100
            price = price - p
            return price
        else:
            return 0

    def __str__(self):
        return str(self.name)  

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    message = models.TextField()
    
    def __str__(self):
        return self.first_name              