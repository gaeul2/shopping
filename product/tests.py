from django.test import TestCase
from rest_framework.test import APIRequestFactory

#표준 RequestFactory API를 사용하여 폼 POST 요청 생성
class ProductTest(TestCase):
    def test_product_create(self):
        #Given
        factory = APIRequestFactory()
        request = factory.post('/user/login/',
                               {
                                    "username" : "seller_user1",
                                    "password" : "1234"
                                })

        #when
        factory = APIRequestFactory()
        request = factory.post('/product/machine/1',
                               {'name' : '스타벅스 이탈리안 스타일 로스팅',
                                'explain' : '네스프레소 호환캡슐, 진한맛을 좋아하는 이에게',
                                '':''})
