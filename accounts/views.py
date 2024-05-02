from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import ParseError
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from .models import User
from .serializers import UserSerializer, ProfileSerializer, ProfileUpdateSerializer
from .permissions import IsOwnerOrReadOnly


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


class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        token = RefreshToken(request.data.get("refresh"))
        token.blacklist()
        return Response({"ok": "Bye!"}, status=status.HTTP_200_OK)


class PasswordChangeAPIView(APIView):
    pass


class ProfileAPIView(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, username):
        profile = get_object_or_404(User, username=username)
        self.check_object_permissions(self.request, profile)
        return profile

    def get(self, request, username):
        profile = self.get_object(username)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request, username):
        if request.data.get('email') in User.objects.values('email'):
            raise ParseError('해당 이메일은 사용중입니다.')
        profile = self.get_object(username)
        serializer = ProfileUpdateSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
