from dataclasses import field
from rest_framework import serializers
from product.models import Product as ProductModel
from product.models import CoffeeMachine as CoffeeMachineModel
from user.serializers import UserSerializer
from product.models import Review as ReviewModel
from product.models import Like as LikeModel
from product.models import ProductOption as ProductOptionModel





class CoffeeMachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeeMachineModel
        fields = ["brand", ]

class ProductOptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductOptionModel
        fields = ["name", "content","price"]


class ProductSerializer(serializers.ModelSerializer):
    options = serializers.ListField(required=False)
    option = ProductOptionSerializer(many=True, read_only=True) #Foriegn Key를 Serializer사용해야 뒤탈없음

    class Meta:
        model = ProductModel
        fields = ["seller", "name", "explain", "thumbnail", "detail_img", "machine", "options","option","created_at", "updated_at"]

    def create(self, validated_data):
        options = validated_data.pop('options')[0]

        # product 모델생성
        product = ProductModel(**validated_data)
        product.save()

        #상품 옵션 생성
        product_option= ProductOptionModel.objects.create(product=product,
                                                          option_name=options[0],
                                                          content=options[1],
                                                          price=int(options[2]))
        product_option.save()
        return product

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance


class ProductInfoSerializer(serializers.ModelSerializer):
    seller = UserSerializer()
    machine = CoffeeMachineSerializer()

    class Meta:
        model = ProductModel
        fields = ["seller", "machine", "name", "explain", "productoption_set","thumbnail", "detail_img"]


class SimpleProductSerializer(serializers.ModelSerializer):
    seller = UserSerializer()

    class Meta:
        model = ProductModel
        fields = ["seller", "name"]


class ReviewSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    product = SimpleProductSerializer()

    class Meta:
        model = ReviewModel
        fields = ["author", "product", "rate", "content", "created_at", "updated_at"]

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


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeModel
        fields = ["user", "product"]

    def create(self, validated_data):
        like = LikeModel(**validated_data)
        like.save()
        return like
