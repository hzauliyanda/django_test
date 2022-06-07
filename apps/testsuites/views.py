from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from . import serializers
from testsuites.models import Testsuits


class TestSuitsViewSet(viewsets.ModelViewSet):
    """
        create:
        创建套件数据

        list:
        获取套件列表数据

        retrieve:
        获取套件详情数据

        update:
        更新套件信息

        delete:
        删除套件信息

    """
    queryset = Testsuits.objects.all()
    serializer_class = serializers.TestsuiteModelSerializer
    permission_classes = [permissions.IsAuthenticated]
