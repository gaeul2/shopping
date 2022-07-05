from functools import partial
from itertools import product
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from product.serializers import LikeSerializer, ProductSerializer, ProductInfoSerializer, ReviewSerializer
from rest_framework import permissions
from product.models import Product as ProductModel
from product.models import CoffeeMachine as CoffeeMachineModel
from product.models import Review as ReviewModel
from product.models import Like as LikeModel
from django.db import transaction


# Create your views here.

class Selling_can_seller_and_Admin(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_admin or request.user.is_seller and request.user.is_authenticated)


# Done 판매자/관리자만 등록할 수 있도록 하기
class ProductView(APIView):
    permission_classes = [Selling_can_seller_and_Admin]

    def post(self, request, category_id):  # 카테고리 별 상품 등록위해 카테고리 id를 받음
        # 1 -> 일리 2-> 네스프레소 3-> 네스카페 돌체구스토 4 ->라바짜

        request.data['seller'] = request.user.id
        request.data['machine'] = category_id

        product_serializer = ProductSerializer(data=request.data)
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(f'{product_serializer.data["name"]} 상품이 등록되었습니다.', status=status.HTTP_200_OK)
        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, product_id):
        product = ProductModel.objects.get(id=product_id)
        print(product)
        if request.user == product.seller:
            edit_serializer = ProductSerializer(product, data=request.data, partial=True)
            if edit_serializer.is_valid():
                edit_serializer.save()
                return Response(edit_serializer.data, status=status.HTTP_200_OK)
            return Response(edit_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(f'잘못된 접근입니다.')

    def delete(self, request, product_id):
        try:
            product = ProductModel.objects.get(id=product_id)
            if request.user == product.seller or request.user.is_admin:
                product.delete()
                product.save()
                return Response(f'{product.name}상품이 삭제되었습니다.')
            return Response(f'작성자만 지울 수 있습니다.')
        except:
            return Response(f'잘못된 접근입니다.')


# Done caffeemachine 별 조회
class ProductShowView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, category_id):
        machine = CoffeeMachineModel.objects.get(id=category_id)
        products_serializer = ProductInfoSerializer(ProductModel.objects.filter(machine=machine), many=True)
        return Response(products_serializer.data, status=status.HTTP_200_OK)


# 리뷰달기
# 1 상세페이지조회 젤 마지막 (완)
# 2. 리뷰 등록하자 (완)
# 3. 수정 삭제(완)
# 4. 권한 부여
class ReviewView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, product_id):
        reviews = ReviewModel.objects.filter(product_id=product_id)
        review_serializer = ReviewSerializer(reviews, many=True)
        return Response(review_serializer.data, status=status.HTTP_200_OK)

    def post(self, request, product_id):
        try:
            product = ProductModel.objects.get(id=product_id)
        except ProductModel.DoesNotExist:
            return Response(f'잘못된 접근입니다.')
        else:
            request.data['author'] = request.user.id
            request.data['product'] = product.id
            review_serializer = ReviewSerializer(data=request.data)
            if review_serializer.is_valid():
                review_serializer.save()
                return Response(f'{product.name}에 대한 {request.user.fullname} 님의 리뷰가 등록되었습니다.',
                                status=status.HTTP_200_OK)
            return Response(review_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, product_id, review_id):
        product = ProductModel.objects.get(id=product_id)
        review = ReviewModel.objects.get(id=review_id)
        if request.user.id == review.author.id:
            review_serializer = ReviewSerializer(review, data=request.data, partial=True)
            if review_serializer.is_valid():
                review_serializer.save()
                return Response({"msg": f'리뷰수정이 완료되었습니다.'}, status=status.HTTP_200_OK)
            return Response(review_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"msg": f'리뷰 작성자만 리뷰수정이 가능합니다.'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, product_id, review_id):
        try:
            product = ProductModel.objects.get(id=product_id)
            review = ReviewModel.objects.get(id=review_id)
        except ProductModel.DoesNotExist:
            return Response({"msg": f'잘못된 요청입니다.'}, status=status.HTTP_400_BAD_REQUEST)
        except ReviewModel.DoesNotExist:
            return Response({"msg": f'잘못된 요청입니다.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            if request.user.id == review.author.id:
                review.delete()
                review.save()
                return Response({"msg": f'리뷰삭제가 완료되었습니다.'}, status=status.HTTP_200_OK)
            return Response({"msg": f'잘못된 요청입니다.'}, status=status.HTTP_400_BAD_REQUEST)


# todo
# 좋아요 
# 권한설정 (로그인한 사용자)
class LikeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @transaction.atomic()
    def post(self, request, product_id):
        request.data['user'] = request.user.id
        request.data['product'] = product_id

        product = ProductModel.objects.get(id=product_id)

        try:  # 이미 존재하는 좋아요라면 삭제/ 존재하지 않는다면 생성
            exist_like = LikeModel.objects.get(user=request.user.id, product=product_id)
        except LikeModel.DoesNotExist:
            like_serializer = LikeSerializer(data=request.data)
            if like_serializer.is_valid():
                like_serializer.save()
                product.like_count += 1
                product.save()
                print(product.like_count)
                return Response({"msg": "좋아요 성공!"}, status=status.HTTP_200_OK)
            return Response(like_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            exist_like.delete()

            product.like_count -= 1
            product.save()
            return Response({"msg": "좋아요 삭제!"})
