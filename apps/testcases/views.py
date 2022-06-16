import json
import os
from datetime import datetime
# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from interfaces.models import Interfaces
from testcases.models import Testcases
from utils import handle_datas, common
from utils.mixins import RunMixin
from . import serializers


class TestcasesViewSet(RunMixin, viewsets.ModelViewSet):
    """
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
    queryset = Testcases.objects.all()
    serializer_class = serializers.TestcasesModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # 格式化instance.include为json类型
        try:
            testcase_include = json.loads(instance.include)
        except Exception:
            testcase_include = dict()
        # 获取项目id
        project_id = Interfaces.objects.get(id=instance.interface_id).project_id
        # 格式化instance.request为json类型
        try:
            testcase_request = json.loads(instance.request)
        except Exception:
            return Response({'msg': '用例格式有误', 'status': 400}, status=400)
        testcase_request_data = testcase_request.get("test").get("request")
        # 获取json参数
        json_data = testcase_request_data.get('json')
        json_data_str = json.dumps(json_data, ensure_ascii=False)

        # 获取extract参数
        extract_data = testcase_request.get('test').get('extract')
        extract_data = handle_datas.handle_data3(extract_data)

        # 获取validate参数
        validate_data = testcase_request.get('test').get('validate')
        validate_data = handle_datas.handle_data1(validate_data)

        # 获取variables参数
        variables_data = testcase_request.get('test').get('variables')
        variables_data = handle_datas.handle_data2(variables_data)

        # 获取parameters参数
        parameters_data = testcase_request.get('test').get('parameters')
        parameters_data = handle_datas.handle_data3(parameters_data)

        # 获取setup_hooks参数
        setup_hooks_data = testcase_request.get('test').get('setup_hooks')
        setup_hooks_data = handle_datas.handle_data5(setup_hooks_data)

        # 获取teardown_hooks参数
        teardown_hooks_data = testcase_request.get('test').get('teardown_hooks')
        teardown_hooks_data = handle_datas.handle_data5(teardown_hooks_data)

        data = {
            "author": instance.author,
            "testcase_name": instance.name,
            "selected_configure_id": testcase_include.get('config'),
            "selected_interface_id": instance.interface_id,
            "selected_project_id": project_id,
            "selected_testcase_id": testcase_include.get('testcases'),
            "method": testcase_request_data.get("method"),
            "url": testcase_request_data.get("url"),
            "param": handle_datas.handle_data4(testcase_request_data.get('params')),
            "header": handle_datas.handle_data4(testcase_request_data.get('headers')),
            "variable": handle_datas.handle_data2(testcase_request_data.get('data')),
            "jsonVariable": json_data_str,
            "extract": extract_data,
            "validate": validate_data,
            "globalVar": variables_data,
            "parameterized": parameters_data,
            "setupHooks": setup_hooks_data,
            "teardownHooks": teardown_hooks_data
        }

        return Response(data, status=200)

    def get_testcase_qs(self):
        """
        获取测试用例集
        :return: 测试用例集,类型为List
        """
        return [self.get_object()]

    def get_serializer_class(self):
        """
        重写父类方法，根据不同action获取对应的序列化器类
        :return:
        """
        if self.action == "run":
            return serializers.TestcaseRunSerializer
        else:
            return super().get_serializer_class()
