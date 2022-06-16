# -*- coding: utf-8 -*-
# @Date    : 2022/4/27 上午8:35
# @Author  : Cristiano Ronalda
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler


class RegisterSerializer(serializers.ModelSerializer):
    """
    定义模型序列化器类
    password_confirm：确认密码
    token：生成token
    """
    password_confirm = serializers.CharField(label='确认密码', help_text='确认密码',
                                             min_length=6, max_length=20, write_only=True,
                                             error_messages={
                                                 'min_length': '仅允许6~20个字符的确认密码',
                                                 'max_length': '仅允许6~20个字符的确认密码',
                                             })
    token = serializers.CharField(label='生成token', help_text='生成token', read_only=True)

    class Meta:
        """
        model：指定序列化模型类
        fields：指定序列化器字段
        extra_kwargs：微调序列化字段的规则
        """
        model = User
        fields = ('id', 'username', 'password', 'email', 'password_confirm', 'token')
        extra_kwargs = {
            'username': {
                'label': '用户名',
                'help_text': '用户名',
                'min_length': 6,
                'max_length': 20,
                'error_messages': {
                    'min_length': '仅允许6-20个字符的用户名',
                    'max_length': '仅允许6-20个字符的用户名',
                }
            },
            'email': {
                'label': '邮箱',
                'help_text': '邮箱',
                'write_only': True,
                'required': True,
                # 添加邮箱重复校验
                'validators': [UniqueValidator(queryset=User.objects.all(), message='此邮箱已注册')],
            },
            'password': {
                'label': '密码',
                'help_text': '密码',
                'write_only': True,
                'min_length': 6,
                'max_length': 20,
                'error_messages': {
                    'min_length': '仅允许6-20个字符的密码',
                    'max_length': '仅允许6-20个字符的密码',
                }
            }
        }

    def validate(self, attrs):
        """
        校验密码与确认密码是否一致
        :param attrs:
        :return:
        """
        if attrs.get('password') != attrs.get('password_confirm'):
            raise serializers.ValidationError
        attrs.pop('password_confirm')
        return attrs

    def create(self, validated_data):
        """
        重写父类方法，创建用户数据的同时，输出token
        :param validated_data:
        :return:
        """
        user = User.objects.create(**validated_data)
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        user.token = token
        return user


# class UserPartSerializer(serializers.ModelSerializer):
#     """
#     定义模型序列化器类,只返回部分字段
#     """
#
#     class Meta:
#         """
#         model：指定序列化模型类
#         fields：指定序列化器字段
#         extra_kwargs：微调序列化字段的规则
#         """
#         model = User
#         fields = ('username', 'is_superuser', 'email', 'date_joined', 'last_login')
