from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from user.serializers import SignupSerializer, InActiveUserSerializer
from user.models import User as UserModel
from rest_framework import status
from rest_framework import permissions
from django.contrib.auth import authenticate
from django.contrib import auth



# Create your views here.
#todo 일반사용자/판매자 분류하기
class UserSignupView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        signup_serializer = SignupSerializer(data=request.data)
        if signup_serializer.is_valid():
            signup_serializer.save()
            return Response(signup_serializer.data, status=status.HTTP_200_OK)
        return Response(signup_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InActiveUserView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self,request):
        users = UserModel.object.filter(is_active=0).all()
        inactive_user_serializer = InActiveUserSerializer(users, many=True)
        return Response(inactive_user_serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        user_list = []
        for i in request.data['pk']:
            user = UserModel.object.get(id=i)
            user.is_active = 1
            user.save()
            user_list.append(user)

        update_user_serializer = InActiveUserSerializer(user_list, many=True)
        return Response(update_user_serializer.data, status=status.HTTP_200_OK)


#Done 미승인시 로그인안됨
class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user is not None:
            auth.login(request,user)
            return Response(f'{user.fullname}님이 로그인 되었습니다.')
        return Response({"msg":'사용자가 존재하지 않거나 아직 승인 심사중입니다.'})



class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user = request.user
        auth.logout(request)
        return Response(f'{user.fullname}님이 로그아웃 되었습니다.')

