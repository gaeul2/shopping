from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from product.serializers import ProductSerializer, ProductInfoSerializer
from rest_framework import permissions
from product.models import Product as ProductModel
# Create your views here.

class Selling_can_seller_and_Admin(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_admin or request.user.is_seller and request.user.is_authenticated )



#Done 판매자/관리자만 등록할 수 있도록 하기
class ProductView(APIView):
    permission_classes = [Selling_can_seller_and_Admin]

    def post(self,request,id): #카테고리 별 상품 등록위해 카테고리 id를 받음
        #1 -> 일리 2-> 네스프레소 3-> 네스카페 돌체구스토 4 ->라바짜
        request.data['seller'] = request.user.id
        request.data['machine'] = id

        product_serializer = ProductSerializer(data= request.data)
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(f'{product_serializer.data["name"]} 상품이 등록되었습니다.', status=status.HTTP_200_OK)
        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self,request,id):
        product = ProductModel.objects.get(id=id)
        print(product)
        if request.user == product.seller:
            edit_serializer = ProductSerializer(product, data=request.data, partial=True)
            if edit_serializer.is_valid():
                edit_serializer.save()
                return Response(edit_serializer.data, status=status.HTTP_200_OK)
            return Response(edit_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        return Response(f'잘못된 접근입니다.')

    def delete(self,request,id):
        try:
            product=ProductModel.objects.get(id=id)
            if request.user == product.seller or request.user.is_admin:
                product.delete()
                product.save()
                return Response(f'{product.name}상품이 삭제되었습니다.')
            return Response(f'작성자만 지울 수 있습니다.')
        except:
            return Response(f'잘못된 접근입니다.')

#Todo caffeemachine 별 조회
class ProductShowView(APIView):
    def get(self, request, id):
        products_serializer = ProductInfoSerializer(ProductModel.objects.all(), many=True)
        return Response(products_serializer.data, status = status.HTTP_200_OK)