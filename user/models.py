# from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, PermissionsMixin
from django.db import models

from .managers import UserManager

# Create your models here.
# class CustomUser(AbstractUser):
#     class Meta:
#         db_table = 'auth_user'
#     username = None
#     email = models.EmailField(unique=True)
# 
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
# 
#     objects = UserManager()

class CustomUser(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = 'auth_user'

    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    groups = None
    user_permissions = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
