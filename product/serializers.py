from dataclasses import field
from rest_framework import serializers
from product.models import Product as ProductModel
from product.models import CoffeeMachine as CoffeeMachineModel
from user.serializers import UserSerializer
from user.models import Review as ReviewModel

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
        fields = ["seller", "machine", "name", "explain", "thumbnail", "detail_img"]

class SimpleProductSerializer(serializers.ModelSerializer):
    seller = UserSerializer()
    class Meta:
        model = ProductModel
        fields = ["seller","name"]

        
class ReviewSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    product = SimpleProductSerializer()
    class Meta:
        model = ReviewModel
        fields = ["author","product","rate","content","created_at", "updated_at"]

    def create(self, validated_data): 
        review = ReviewModel(**validated_data)
        print(validated_data)
        review.save()
        return review

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance
