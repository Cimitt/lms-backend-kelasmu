from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from accounts.models import User
from api.auth.serializerss import UserSerializer


class AuthViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
