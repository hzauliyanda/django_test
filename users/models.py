from django.contrib.auth.models import User
from django.db import models


# Create your models here.
# class UserModel(User):
#     mobile = models.CharField(max_length=11, unique=True)
#     username = models.CharField(min_length=6, max_length=20, unique=True,
#                                 help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
#                                 error_messages={
#                                     'unique': "A user with that username already exists.",
#                                 }
#                                 )
#     password = models.CharField(min_length=6, max_length=20)
#     confirm_password = models.CharField(min_length=6, max_length=20)
#
#     class Meta:
#         db_table = 'users'
