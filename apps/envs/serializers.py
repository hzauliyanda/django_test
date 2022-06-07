# coding:utf-8
from rest_framework import serializers
from envs.models import Envs


class EnvsModelSerializer(serializers.ModelSerializer):
    """
    环境配置模型序列化器类
    """

    class Meta:
        """
        model：指定序列化模型类
        exclude：指定模型类中update_time不需要转化为序列化器字段
        extra_kwargs：create_time只输出，并且格式化
        """
        model = Envs
        exclude = ('update_time',)
        extra_kwargs = {
            'create_time': {
                'read_only': True,
                'format': '%Y年%m月%d日 %H:%M:%S'
            }
        }


class EnvsNamesSerializer(serializers.ModelSerializer):
    """
    序列化器类，生成序列化器字段时只生成id和name
    """
    class Meta:
        model = Envs
        fields = ('id', 'name')
