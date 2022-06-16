# -*- coding: utf-8 -*-
"""
------------------------------
 @Date    : 2022/6/8 上午10:39
 @Author  : Cristiano Ronalda
------------------------------
"""
from rest_framework import serializers
from envs.models import Envs
from interfaces.models import Interfaces
from projects.models import Projects


class ManualValidateIsExist:
    def __init__(self, kw):
        self.kw = kw

    def __call__(self, value):
        if self.kw == 'project':
            if not Projects.objects.filter(id=value).exists():
                raise serializers.ValidationError('项目id不存在')
        elif self.kw == "interface":
            if not Interfaces.objects.filter(id=value).exists():
                raise serializers.ValidationError("接口id不存在")
        elif self.kw == "env":
            if not Envs.objects.filter(id=value).exists():
                raise serializers.ValidationError("环境配置id不存在")

