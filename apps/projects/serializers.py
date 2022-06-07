# coding:utf-8
"""
序列化器，子应用中创建serializers.py文件
"""
from rest_framework import serializers
from .models import Projects
from interfaces.models import Interfaces

from debugtalks.models import DebugTalks


class ProjectsModelSerializer(serializers.ModelSerializer):
    """
    定义项目模型序列化器类
    """
    class Meta:
        """
        model：指定序列化模型类
        exclude：指定模型类中update_time不需要转化为序列化器字段
        extra_kwargs：create_time只输出，并且格式化
        """
        model = Projects
        exclude = ('update_time',)
        extra_kwargs = {
            'create_time': {
                'read_only': True,
                'format': '%Y年%m月%d日 %H时%M分%S秒'
            }
        }

    def create(self, validated_data):
        """
        重写父类方法，创建项目时同步创建DebugTalks文件
        :param validated_data:
        :return:
        """
        insyance = super().create(validated_data)
        DebugTalks.objects.create(project=insyance)
        return insyance


class ProjectsNamesModelSerailizer(serializers.ModelSerializer):
    """
    序列化器类，生成序列化器字段时只生成项目的id和name
    """
    class Meta:
        model = Projects
        fields = ('id', 'name')


class InterfacesNamesModelSerailizer(serializers.ModelSerializer):
    """
    序列化器类，生成序列化器字段时只生成接口的id和name
    """
    class Meta:
        model = Interfaces
        fields = ('id', 'name')


class ProjectInterfacesModelSerailizer(serializers.ModelSerializer):
    """
    1、interfaces为通过父表获取从表数据，因为表定义字段时指定类related_name为interfaces，那么就用这个指定的名字
    2、又把序列化器InterfacesNamesModelSerailizer输出的数据包了一层
     输出实例：{
    "interfaces": [{"id": 1,
            "name": "登录接口-正向用例"}]
        }
    """
    interfaces = InterfacesNamesModelSerailizer(label='所属项目的接口信息', help_text='所属项目的接口信息', read_only=True, many=True)

    class Meta:
        model = Projects
        fields = ('interfaces',)
