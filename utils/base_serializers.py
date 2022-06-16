# -*- coding: utf-8 -*-
"""
------------------------------
 @Date    : 2022/6/16 上午11:35
 @Author  : Cristiano Ronalda
------------------------------
"""
from rest_framework import serializers
from utils.validators import ManualValidateIsExist


class RunSerializer(serializers.ModelSerializer):
    """
    封装为基础序列化器类，生成序列化器字段时只生成id和name
    """
    env_id = serializers.IntegerField(label="所属环境id", help_text="所属环境id",
                                      validators=[ManualValidateIsExist('env')])

    class Meta:
        model = None
        fields = ('id', 'env_id')