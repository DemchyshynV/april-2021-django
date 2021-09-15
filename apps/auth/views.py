from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from utils.jwt_utils import JwtUtils
from django.contrib.auth import get_user_model
from apps.user.models import CustomUser

UserModel: CustomUser = get_user_model()


class ActivateView(GenericAPIView):
    permission_classes = (AllowAny,)

    def get(self, *args, **kwargs):
        token = kwargs.get('token')
        JwtUtils.validate_token(token)
        UserModel.objects.activate()
        return Response(status=status.HTTP_200_OK)
