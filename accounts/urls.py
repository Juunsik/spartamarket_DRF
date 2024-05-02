from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView,
)
from . import views

urlpatterns = [
    path("", views.SignupAPIView.as_view()),
    path("login/", views.LoginAPIView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("<str:username>/", views.ProfileAPIView.as_view()),
    path("auth/logout/", views.LogoutAPIView.as_view()),
    path("password/", views.PasswordChangeAPIView.as_view()),
]
