from django.urls import path
from product import views


urlpatterns =[
    path('product/add', views.ProductView.as_view(), name='add_product'),
    path('product/update/<int:id>', views.ProductView.as_view(), name='edit_product'),
    path('product/delete/<int:id>', views.ProductView.as_view(), name='delete_product'),
    path('product/show', views.ProductShowView.as_view(), name='show_products'),
]