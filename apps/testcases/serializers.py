# coding:utf-8
from rest_framework import serializers
from interfaces.models import Interfaces
from testcases.models import Testcases


class InterfaceProjectModelSerializer(serializers.ModelSerializer):
    """
    定义项目模型序列化器类
    project：所属的项目名称（SlugRelatedField是取Projects模型中name字段作为该字段的值，即序列化输出为Projects表的name）
    pid：所属项目id
    iid：所属接口id
    """
    project = serializers.SlugRelatedField(label='所属的项目名称', help_text='所属的项目名称', read_only=True, slug_field='name')
    pid = serializers.IntegerField(label='所属项目id', help_text='所属项目id', write_only=True, validators=[])
    iid = serializers.IntegerField(label='所属接口id', help_text='所属接口id', write_only=True, validators=[])

    class Meta:
        """
        model：指定序列化模型类
        fields：指定模型类中的序列化器字段
        extra_kwargs：name只输出
        """
        model = Interfaces
        fields = ('name', 'project', 'pid', 'iid')
        extra_kwargs = {
            'name': {
                'read_only': True,
            }
        }

    def validate(self, attrs):
        # TODO
        return attrs


class TestcasesModelSerializer(serializers.ModelSerializer):
    interface = InterfaceProjectModelSerializer(label='所属项目和接口信息', help_text='所属项目和接口信息')

    class Meta:
        model = Testcases
        exclude = ('create_time', 'update_time')
        extra_kwargs = {
            'request': {
                'write_only': True,
            },
            'include': {
                'write_only': True
            }
        }

    def validate_request(self, attr):
        # TODO
        return attr

    def validate(self, attrs):
        # TODO
        return attrs

    def to_internal_value(self, data):
        result = super().to_internal_value(data)
        # TODO
        return result
