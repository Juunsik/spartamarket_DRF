from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from .models import User
from .serializers import UserSerializer, ProfileSerializer


# Create your views here.
class SignupAPIView(APIView):
    def post(self, request):
        password = request.data.get("password")
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            user.set_password(password)
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)
        if user is None:
            return Response(
                {"message": "아이디 또는 비밀번호가 일치하지 않습니다."},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        refresh = RefreshToken.for_user(user)
        update_last_login(None, user)

        return Response(
            {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            },
            status=status.HTTP_200_OK,
        )

class ProfileAPIView(APIView):
    permission_classes=[IsAuthenticated]
    
    def get_object(self, username):
        return get_object_or_404(User, username=username)
    
    def get(self, request, username):
        profile=self.get_object(username)
        serializer=ProfileSerializer(profile)
        return Response(serializer.data)