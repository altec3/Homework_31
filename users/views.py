from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from users.models import User
from users.serializers import UserListSerializer, UserCreateSerializer, UserRetrieveSerializer, UserUpdateSerializer, \
    UserDestroySerializer


class UsersListView(ListAPIView):
    """Get all users"""
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class UserCreateView(CreateAPIView):
    """Create a new user"""
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserDetailView(RetrieveAPIView):
    """Get user by pk"""
    queryset = User.objects.all()
    serializer_class = UserRetrieveSerializer


class UserUpdateView(UpdateAPIView):
    """Update user given its identifier"""
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer


class UserDeleteView(DestroyAPIView):
    """Delete user given its identifier"""
    queryset = User.objects.all()
    serializer_class = UserDestroySerializer
