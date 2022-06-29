from rest_framework import serializers
from product.models import Category as CategoryModel
from product.models import Product as ProductModel
from product.models import CoffeeMachine as CoffeeMachineModel
from user.serializers import UserSerializer



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ["name",]


class CoffeeMachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeeMachineModel
        fields = ["brand", ]


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductModel
        fields = ["seller","name", "explain", "thumbnail", "detail_img", "category", "machine","created_at", "updated_at"]


    def create(self, validated_data):
        category = validated_data.pop('category')
        machine = validated_data.pop('machine')

        #product 모델생성
        product = ProductModel(**validated_data)
        print(validated_data)
        product.machine = machine
        product.save()
        for i in category:
            product.category.add(i)
        product.save()

        return product


    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance,key,value)

        instance.save()
        return instance

class ProductInfoSerializer(serializers.ModelSerializer):
    seller = UserSerializer()
    machine = CoffeeMachineSerializer()
    category = CategorySerializer()

    class Meta:
        model = ProductModel
        fields = ["seller","name", "explain", "thumbnail", "detail_img", "category", "machine", "created_at", "updated_at"]




