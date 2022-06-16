from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from utils.mixins import RunMixin
from .models import Interfaces
from . import serializers
from testcases.models import Testcases

from configures.models import Configures


class InterfacesViewSet(RunMixin, viewsets.ModelViewSet):
    """
        create:
        创建接口数据

        list:
        获取接口列表数据

        retrieve:
        获取接口详情数据

        update:
        更新接口信息

        delete:
        删除接口信息

        testcases:
        获取接口测试用例

        configures:
        获取接口配置信息

    """
    queryset = Interfaces.objects.all()
    serializer_class = serializers.InterfacesModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        """
        重写list方法，增加返回testcases和configures数据
        testcases：为接口的测试用例信息
        configures：为接口的配置信息
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        response = super().list(request, *args, **kwargs)
        for item in response.data['results']:
            item['testcases'] = Testcases.objects.filter(interface_id=item.get('id')).count()
            item['configures'] = Configures.objects.filter(interface_id=item.get('id')).count()
        return response

    @action(detail=True)
    def testcases(self, request, *args, **kwargs):
        """
        获取接口的测试用例信息
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        response = super().retrieve(request, *args, **kwargs)
        response.data = response.data.get('testcases_set')
        return response

    @action(detail=True)
    def configures(self, request, *args, **kwargs):
        """
         获取接口的配置信息
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        response = super().retrieve(request, *args, **kwargs)
        response.data = response.data.get('configures')
        return response

    def get_testcase_qs(self):
        """
        获取测试用例集
        :return: 测试用例集,类型为QuerySet
        """
        instance = self.get_object()
        qs = Testcases.objects.filter(interface=instance)
        return qs

    def get_serializer_class(self):
        """
        重写父类方法，根据不同action调用不同的序列化器类
        :return:
        """
        if self.action == 'testcases':
            return serializers.TestcasesInterfacesModelSerializer
        elif self.action == 'configures':
            return serializers.ConfiguresInterfacesModelSerializer
        elif self.action == 'run':
            return serializers.InterfacesRunModelSerializer
        else:
            return super().get_serializer_class()
