from django.db import models

# Create your models here.

class CoffeeMachine(models.Model): # 카테고리
    brand = models.CharField("커피머신 브랜드", max_length=100)

    def __str__(self):
        return self.brand

class Product(models.Model): #커피캡슐
    seller = models.ForeignKey('user.User', on_delete=models.CASCADE)
    machine = models.ForeignKey(CoffeeMachine, on_delete=models.CASCADE)
    name = models.CharField("캡슐이름", max_length=100)
    explain = models.TextField("캡슐설명")
    thumbnail = models.FileField(upload_to='product/thumbnail')
    detail_img = models.FileField(upload_to='product/detail')
    like_count = models.IntegerField("좋아요 갯수", default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ProductOption(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField("옵션이름", max_length=50)
    content = models.TextField("옵션내용")
    price = models.IntegerField("가격")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    product_option = models.ForeignKey(ProductOption, on_delete=models.CASCADE)
    count = models.IntegerField("갯수")
    is_paid = models.BooleanField(default=1) # 결제하면 0으로 바꾸자
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user}의 장바구니'

class OrderList(models.Model):
    buyer = models.ForeignKey('user.User', on_delete=models.CASCADE)
    product_option = models.ForeignKey(ProductOption, on_delete=models.CASCADE)
    pay_type = models.CharField("결제방식", max_length=80)
    total_price = models.IntegerField("총금액")
    state = models.CharField("주문상태", max_length=90) #결제완료,배송중,배송완료
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user}의 구매내역'


class Review(models.Model):
    author = models.ForeignKey('user.USer', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rate = models.IntegerField("평점")
    content = models.TextField("리뷰 내용")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f'{self.author}가 작성한 {self.product}에 대한 리뷰'


class Like(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE) 
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    #중복 좋아요 방지 위한 user와 product에 제한걸기
    #user/product는 pk값이 들어오므로 같은 pk로 같은 product_pk에 좋아요못함
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user","product"],
                                    name='unique_like')
        ]