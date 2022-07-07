from django.urls import path
from product import views


urlpatterns =[
    path('', views.showindex, name='index'),
    # 카테고리별 상품 등록/수정/제거/조회
    path('product/machine/<int:category_id>', views.ProductView.as_view(), name='add_product'),
    path('product/<int:product_id>', views.ProductView.as_view(), name='edit_product'),
    path('product/<int:product_id>', views.ProductView.as_view(), name='delete_product'),
    path('product/machine/<int:category_id>', views.ProductShowView.as_view(), name='products_by_machine'),

    #상품 상세페이지 + 리뷰조회,
    path('product/detail/<int:product_id>', views.ProductDetailView.as_view(), name='product_detail'),
    # todo 상품품절시 판매자가 for sale바꿀수 있게(옵션이 한개이상 있을때만 가능)
    # todo 옵션이 0개여서 for_sale=0 인 상품을 관리자가 열어주기
    #리뷰 등록/제거/수정
    path('product/review/<int:product_id>', views.ReviewEditView.as_view(), name='create_review'),
    path('product/review/<int:product_id>/<int:review_id>', views.ReviewEditView.as_view(), name='edit_review'),

    #찜하기(좋아요)
    path('product/like/<int:product_id>', views.LikeView.as_view(), name='like_product'),

    # 상품 옵션 추가/수정/삭제
    path('product/option/<int:id>',views.ProductOptionEditView.as_view(),name='add_option'),
]