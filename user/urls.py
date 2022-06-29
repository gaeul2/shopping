from django.urls import path
from user import views

urlpatterns = [
   path('user/signup', views.UserSignupView.as_view(), name='signup'),
   path('user/show/inactive', views.InActiveUserView.as_view(), name='show_not_active_user'),
   path('user/update/active', views.InActiveUserView.as_view(), name='activation_user'),
   path('user/login', views.LoginView.as_view(), name='login'),
   path('user/logout', views.LogoutView.as_view(), name='logout'),
]