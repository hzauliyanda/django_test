# coding:utf-8
import json
import re
from rest_framework import serializers
from interfaces.models import Interfaces
from projects.models import Projects
from utils.base_serializers import RunSerializer
from utils.validators import ManualValidateIsExist
from .models import Testsuits


class TestsuiteModelSerializer(serializers.ModelSerializer):
    """
    定义模型序列化器类
    project为所属的项目名称
    project_id为所属的项目id
    """

    project = serializers.StringRelatedField(label='所属的项目名称', help_text='所属的项目名称')
    project_id = serializers.PrimaryKeyRelatedField(queryset=Projects.objects.all(), label='所属的项目id',
                                                    help_text='所属的项目id')

    class Meta:
        """
        model：指定序列化模型类
        fields：所有字段均为序列化器字段
        extra_kwargs：create_time和update_time都只输出，并且格式化
        """
        model = Testsuits
        fields = '__all__'
        extra_kwargs = {
            "create_time": {
                "read_only": True,
                "format": "%Y年%m月%d日 %H:%M:%S"
            },
            "update_time": {
                "read_only": True,
                "format": "%Y年%m月%d日 %H:%M:%S"
            },
        }

    def validate_include(self, attr):
        """
        自定义校验方法，校验include内容是否满足格式要求
        :param attr:
        :return:
        """
        print('validate_include的attr：' + attr)
        result = re.match(r'^\[\d+(, *\d+)*\]$', attr)
        if result is None:
            raise serializers.ValidationError('include参数格式有误')

        result = result.group()
        try:
            data = json.loads(result)
        except Exception:
            raise serializers.ValidationError('include参数格式有误')

        for item in data:
            if not Interfaces.objects.filter(id=item).exists():
                raise serializers.ValidationError('接口id不存在')
        return attr

    def to_internal_value(self, data):
        """
        重写父类方法，在所有字段开始进行校验之前更新project_id的值
        :param data:
        :return:
        """
        tmp = super().to_internal_value(data)
        tmp['project_id'] = tmp.get('project_id').id
        return tmp


class TestsuiteRunSerializer(RunSerializer, serializers.ModelSerializer):
    """
    继承父类BaseSerializer
    """

    class Meta(RunSerializer.Meta):
        """
        继承父类BaseSerializer的子类，指定模型对象
        """
        model = Testsuits
