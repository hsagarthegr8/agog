from rest_framework.generics import ListAPIView,RetrieveDestroyAPIView,CreateAPIView
from rest_framework.permissions import AllowAny

from accounts.models import User
from .serializers import UserSerializer,UserCreateSerializer


class UserCreate(CreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = (AllowAny,)


class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

