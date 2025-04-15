from django.urls import path
from rest_framework_simplejwt.views import (
    TokenBlacklistView,
    TokenObtainPairView,
    TokenRefreshView,
)

from authentication.views.register_view import RegisterView
from authentication.views.user_view import UserViewSet

urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("logout/", TokenBlacklistView.as_view(), name="token_blacklist"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", RegisterView.as_view(), name="auth_register"),
    path("user/", UserViewSet.as_view({"get": "list"}), name="user-list"),
]
