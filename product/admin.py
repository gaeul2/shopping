from django.contrib import admin
from product.models import Product as ProductModel
from product.models import CoffeeMachine as CoffeeMachineModel

# Register your models here.
admin.site.register(ProductModel)
admin.site.register(CoffeeMachineModel)