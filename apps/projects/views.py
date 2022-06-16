# Create your views here.
from datetime import datetime

from django.db.models import Sum
from django.views import View
from rest_framework import status, filters, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from debugtalks.models import DebugTalks
from envs.models import Envs
from reports.models import Reports
from utils.mixins import RunMixin
from . import serializers
from .models import Projects
from rest_framework import viewsets
import logging
from interfaces.models import Interfaces
from testsuites.models import Testsuits
from testcases.models import Testcases
from configures.models import Configures

log = logging.getLogger('wl')


class ProjectViewSet(RunMixin, viewsets.ModelViewSet):
    """
    create:
    创建项目数据

    list:
    获取项目列表数据

    retrieve:
    获取项目详情数据

    update:
    更新项目信息

    names:
    获取项目名称

    interfaces:
    获取项目所属接口信息

    """
    queryset = Projects.objects.all()
    serializer_class = serializers.ProjectsModelSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['=name', '=leader', '=id']
    ordering_fields = ['id', 'name', 'leader']
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        """
        查询项目列表
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        response = super().list(self, request, *args, **kwargs)
        for item in response.data['results']:
            item['interfaces'] = Interfaces.objects.filter(project_id=item.get('id')).count()
            item['testsuits'] = Testsuits.objects.filter(project_id=item.get('id')).count()
            # interface__project__id为Testcases的关联字段interface的__关联字段project的id
            item['testcases'] = Testcases.objects.filter(interface__project__id=item.get('id')).count()
            item['configures'] = Configures.objects.filter(interface__project__id=item.get('id')).count()
        log.info("action为list的response：" + str(response.data))
        return response

    @action(methods=['GET'], detail=False)
    def names(self, request, *args, **kwargs):
        """
        只返回id和name字段
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().list(request, *args, **kwargs)

    @action(detail=True)
    def interfaces(self, request, *args, **kwargs):
        """
        查询项目下的接口信息
        :param request:
        :param args: 路径参数pk
        :param kwargs:
        :return:
        """
        result = super().retrieve(request, *args, **kwargs)
        result.data = result.data.get('interfaces')
        return result

    # @action(methods=['POST'], detail=True)
    # def run(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     testcases_qs = Testcases.objects.filter(interface__project=instance)
    #     if len(testcases_qs) == 0:
    #         return Response({'msg': '此项目下没有用例，无法执行！'}, status=400)
    #     return self.execute(request, testcases_qs)
    def get_testcase_qs(self):
        """
        获取测试用例集
        :return: 测试用例集,类型为QuerySet
        """
        instance = self.get_object()
        testcases_qs = Testcases.objects.filter(interface__project=instance)
        return testcases_qs

    def get_serializer_class(self):
        """
        重写get_serializer_class类，根据不同action访问不同的模型序列化器类
        :return:
        """
        if self.action == 'names':
            return serializers.ProjectsNamesModelSerailizer
        elif self.action == 'interfaces':
            return serializers.ProjectInterfacesModelSerailizer
        elif self.action == 'run':
            return serializers.ProjectRunModelSerailizer
        else:
            return super().get_serializer_class()

    def paginate_queryset(self, queryset):
        """
        重写父类方法，action为names时不分页
        :param queryset:
        :return:
        """
        if self.action == 'names':
            return
        else:
            return super().paginate_queryset(queryset)
