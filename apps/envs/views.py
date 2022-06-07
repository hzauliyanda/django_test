from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions

from envs.models import Envs
from utils.mixins import NameMixin
from . import serializers


class EnvsViewSet(NameMixin, viewsets.ModelViewSet):
    """
    内置函数视图集，继承NameMixin，支持的action如下：
    1、names；
    """
    queryset = Envs.objects.all()
    serializer_class = serializers.EnvsModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        """
        重写父类方法，action为names时调用EnvsNamesSerializer
        :return:
        """
        if self.action == 'names':
            return serializers.EnvsNamesSerializer
        else:
            return self.serializer_class
