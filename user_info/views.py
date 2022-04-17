from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import AllowAny,IsAuthenticatedOrReadOnly
from .serializers import UserRegisterSerializer
from .permissions import IsSelfOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    lookup_field = 'username'

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes=[IsAuthenticatedOrReadOnly, IsSelfOrReadOnly]
        return super().get_permissions()