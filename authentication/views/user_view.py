from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from authentication.serializers.user_serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    pagination_class = None
    serializer_class = UserSerializer

    def get_queryset(self):
        return self.request.user

    def list(self, request, *args, **kwargs):
        user = request.user
        user_serializer = UserSerializer(user)

        return Response(
            {"user": user_serializer.data},
            status=status.HTTP_200_OK,
        )
