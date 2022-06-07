# -*- coding: utf-8 -*-
# @Date    : 2022/6/2 下午5:05
# @Author  : Cristiano Ronalda

from rest_framework import serializers
from debugtalks.models import DebugTalks


class DebugTalksModelSerializer(serializers.ModelSerializer):
    """
    DebugTalk模型序列化器类
    SlugRelatedField是取Projects模型中name字段作为该字段的值，即序列化输出为Projects表的name
    """
    project = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        """
        model：指定序列化模型类
        exclude：指定模型类中create_time和update_time不需要转化为序列化器字段
        extra_kwargs：debugtalk只需输入
        """
        model = DebugTalks
        exclude = ('create_time', 'update_time',)
        extra_kwargs = {
            'debugtalk': {
                'write_only': True,
            }
        }


class DebugTalksSerializer(serializers.ModelSerializer):
    """
    序列化器类，生成序列化器字段时只生成id和debugtalk
    """
    class Meta:
        model = DebugTalks
        fields = ('id', 'debugtalk')
