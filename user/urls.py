from django.urls import path
from user import views

urlpatterns = [
   path('signup', views.UserSignupView.as_view(), name='signup'),
   path('login', views.LoginView.as_view(), name='login'),
   path('logout', views.LogoutView.as_view(), name='logout'),
]