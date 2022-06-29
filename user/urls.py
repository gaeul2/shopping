from django.urls import path
from user import views

urlpatterns = [
   path('signup', views.UserSignupView.as_view(), name='signup'),
   path('show', views.IsNotActiveUserView.as_view(), name='show_not_active_user'),
   path('login', views.LoginView.as_view(), name='login'),
   path('logout', views.LogoutView.as_view(), name='logout'),
]