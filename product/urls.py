from django.urls import path
from product import views


urlpatterns =[
    # 카테고리별 상품 등록/수정/제거/조회
    path('product/add/<int:category_id>', views.ProductView.as_view(), name='add_product'),
    path('product/update/<int:product_id>', views.ProductView.as_view(), name='edit_product'),
    path('product/delete/<int:product_id>', views.ProductView.as_view(), name='delete_product'),
    path('product/<int:category_id>', views.ProductShowView.as_view(), name='products_by_machine'),

    #상품 상세페이지 + 리뷰조회,
    path('product/detail/<int:product_id>', views.ProductDetailView.as_view(), name='product_detail'),

    #리뷰 등록/제거/수정
    path('product/review/<int:product_id>', views.ReviewEditView.as_view(), name='create_review'),
    path('product/review/<int:product_id>/<int:review_id>', views.ReviewEditView.as_view(), name='edit_review'),

    #찜하기(좋아요)
    path('product/like/<int:product_id>', views.LikeView.as_view(), name='like_product'),

    # 상품 옵션 추가
    path('product/option/<int:product_id>',views.ProductOptionEditView.as_view(),name='add_option'),
]