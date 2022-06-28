from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from user.serializers import SignupSerializer
from rest_framework import status
from django.contrib.auth import authenticate

# Create your views here.
#todo 일반사용자/판매자 분류하기
class UserSignupView(APIView):
    def post(self, request):
        signup_serializer = SignupSerializer(data=request.data)
        if signup_serializer.is_valid():
            signup_serializer.save()
            return Response(signup_serializer.data, status=status.HTTP_200_OK)
        return Response(signup_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    def post(self, request):
        user = authenticate(username=request.data['username'], password=request.data['password'])
