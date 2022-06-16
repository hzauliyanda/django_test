# coding:utf-8
import json
import re
from rest_framework import serializers

from configures.models import Configures
from interfaces.models import Interfaces
from testcases.serializers import InterfaceProjectModelSerializer


class ConfiguresSerializer(serializers.ModelSerializer):
    """
    定义模型序列化器类
    interface为所属的项目id
    """

    interface = InterfaceProjectModelSerializer(label='所属项目和接口信息', help_text='所属项目和接口信息')

    class Meta:
        """
        model：指定序列化模型类
        fields：所有字段均为序列化器字段
        extra_kwargs：create_time和update_time都只输出，并且格式化
        """
        model = Configures
        fields = ('id', 'name', 'interface', 'author', 'request')
        extra_kwargs = {
            "request": {
                "write_only": True
            },
        }

    def to_internal_value(self, data):
        """
        重写父类方法，在所有字段开始进行校验之前更新interface_id的值
        :param data:
        :return:
        """
        tmp = super().to_internal_value(data)
        iid = tmp.pop('interface').get('iid')
        tmp['interface_id'] = iid
        return tmp
