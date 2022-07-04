from rest_framework import serializers
from product.models import Product as ProductModel
from product.models import CoffeeMachine as CoffeeMachineModel
from user.serializers import UserSerializer


class CoffeeMachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeeMachineModel
        fields = ["brand", ]


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductModel
        fields = ["seller","name", "explain", "thumbnail", "detail_img", "machine","created_at", "updated_at"]
        extra_kwargs = {

        }

    def create(self, validated_data):

        #product 모델생성
        product = ProductModel(**validated_data)
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

    class Meta:
        model = ProductModel
        fields = "__all__"




