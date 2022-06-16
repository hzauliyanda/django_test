import re

from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.decorators import action

from testcases.models import Testcases
from utils.mixins import RunMixin
from . import serializers
from testsuites.models import Testsuits


class TestSuitsViewSet(RunMixin, viewsets.ModelViewSet):
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

    def get_testcase_qs(self):
        """
        获取测试用例集
        :return: 测试用例集,类型为List
        """
        instance = self.get_object()
        testcase_id_list = re.findall('[0-9]', instance.include)
        result = []
        for id in testcase_id_list:
            qs = Testcases.objects.filter(interface_id=id)
            for i in qs:
                result.append(i)
        return result

    def get_serializer_class(self):
        """
        重写父类方法，根据不同action获取对应的序列化器类
        :return:
        """
        if self.action == 'run':
            return serializers.TestsuiteRunSerializer
        else:
            return super().get_serializer_class()
