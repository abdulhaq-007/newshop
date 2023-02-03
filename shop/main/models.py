from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField('Tovar nomi', max_length=150)
    