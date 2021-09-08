from django.contrib.auth import get_user_model

from rest_framework.generics import ListCreateAPIView

from .models import CustomUser
from .serializers import UserSerializer

UserModel: CustomUser = get_user_model()


class UserListCreateView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
