# -*- coding: utf-8 -*-
# @Date    : 2022/6/2 下午2:05
# @Author  : Cristiano Ronalda
import logging
import os
from datetime import datetime

from django.conf import settings
from rest_framework.decorators import action
from rest_framework.response import Response

from envs.models import Envs
from utils import common

log = logging.getLogger('wl')


class NameMixin:

    @action(methods=['GET'], detail=False)
    def names(self, request, *args, **kwargs):
        """
        自定义action动作names
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        response = super().list(request, *args, **kwargs)
        return response

    def paginate_queryset(self, queryset):
        """
        names action禁用分页功能
        :param queryset:
        :return:
        """
        if self.action == 'names':
            return
        else:
            return super().paginate_queryset(queryset)

    def filter_queryset(self, queryset):
        """
        names action禁用过滤功能
        :param queryset:
        :return:
        """
        if self.action == 'names':
            return self.queryset
        else:
            return super().filter_queryset(queryset)


class RunMixin:
    def execute(self, request, qs):
        """
        执行过程封装
        :param request:
        :param qs:
        :return:
        """
        # 1、取出用例模型对象并获取env_id
        instance = self.get_object()  # type:模型类
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        env_id = serializer.validated_data.get('env_id')
        env = Envs.objects.get(id=env_id)
        # 2、创建以时间戳命名的目录
        testcase_dir_path = os.path.join(settings.PROJECT_DIR, datetime.strftime(datetime.now(), "%Y%m%d%H%M%S"))
        # 3、创建以项目名命名的目录
        os.makedirs(testcase_dir_path)
        log.info(f"目录已生成：{testcase_dir_path}")
        # 4、生成debugtalks.py、yaml用例文件
        for obj in qs:
            common.generate_testcase_file(obj, env, testcase_dir_path)
        return common.run_testcase(instance, testcase_dir_path)

    @action(methods=['POST'], detail=True)
    def run(self, request):
        qs = self.get_testcase_qs()
        if len(qs) == 0:
            return Response({'msg': '未找到测试用例'}, status=400)
        return self.execute(request, qs)

    def get_testcase_qs(self):
        return []
        # raise ImportError("")
