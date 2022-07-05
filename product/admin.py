from django.contrib import admin
from product.models import Product as ProductModel
from product.models import CoffeeMachine as CoffeeMachineModel
from product.models import Review as ReviewModel
from product.models import Like as LikeModel


# Register your models here.
admin.site.register(ProductModel)
admin.site.register(CoffeeMachineModel)
admin.site.register(ReviewModel)
admin.site.register(LikeModel)