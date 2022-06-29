from django.contrib import admin
from product.models import Product as ProductModel
from product.models import Category as CategoryModel

# Register your models here.
admin.site.register(CategoryModel)