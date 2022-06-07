from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from users.serializers import RegisterSerializer


class UserView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    create:
    创建接口数据
    """
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class UsernameIsExistedView(APIView):
    """
    重写父类方法，统计数据库中用户名的数量
    """
    def get(self, request, username):
        count = User.objects.filter(username=username).count()
        return Response({'username': username, 'count': count})


class EmailIsExistedView(APIView):
    """
    重写父类方法，统计数据库中email的数量
    """
    def get(self, request, email):
        count = User.objects.filter(email=email).count()
        return Response({'email': email, 'count': count})
