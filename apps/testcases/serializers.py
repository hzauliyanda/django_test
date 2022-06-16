# coding:utf-8
import json
import re
from rest_framework import serializers
from interfaces.models import Interfaces
from testcases.models import Testcases
from utils.base_serializers import RunSerializer
from utils.validators import ManualValidateIsExist


class InterfaceProjectModelSerializer(serializers.ModelSerializer):
    """
    定义项目模型序列化器类
    project：所属的项目名称（SlugRelatedField是取Projects模型中name字段作为该字段的值，即序列化输出为Projects表的name）
    pid：所属项目id
    iid：所属接口id
    """
    project = serializers.SlugRelatedField(label='所属的项目名称', help_text='所属的项目名称',
                                           read_only=True, slug_field='name')
    pid = serializers.IntegerField(label='所属项目id', help_text='所属项目id', write_only=True,
                                   validators=[ManualValidateIsExist('project')])
    iid = serializers.IntegerField(label='所属接口id', help_text='所属接口id', write_only=True,
                                   validators=[ManualValidateIsExist('interface')])

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
        """
        多字段联合校验，校验所属项目id和接口id是否匹配
        :param attrs:所属项目id和接口id
        :return:所属项目id和接口id
        """
        if not Interfaces.objects.filter(id=attrs.get('iid'), project_id=attrs.get('pid')).exists():
            raise serializers.ValidationError("所属项目id和接口id不匹配")
        return attrs


class TestcasesModelSerializer(serializers.ModelSerializer):
    """
    定义模型序列化器类
    interface：把InterfaceProjectModelSerializer类再包一层
    """
    interface = InterfaceProjectModelSerializer(label='所属项目和接口信息', help_text='所属项目和接口信息')

    class Meta:
        """
        model：指定序列化模型类
        exclude：指定模型类中update_time不需要转化为序列化器字段
        extra_kwargs：request和include 输入时校验
        """
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

    def to_internal_value(self, data):
        """
        重写父类方法，重新给interface赋值为Interfaces模型类，才能正确调用create的action写入数据
        :param data:请求数据
        :return:待校验数据
        """
        # {"test":{"name":"登录接口_正向用例","request":{"url":"/user/login/","method":"POST","json":{"username":"$username","password":"$password"}},"variables":[{"username":"keyou1"},{"password":"123456"}],"extract":[{"token":"content.token"}],"validate":[{"check":"status_code","expected":200,"comparator":"equals"}]}}
        result = super().to_internal_value(data)
        iid = result.get('interface').get('iid')
        result['interface'] = Interfaces.objects.get(id=iid)
        return result

    # def validate_request(self, attr):
    #     """
    #     单字段校验，校验request的数据格式
    #     :param attr: 请求中request数据
    #     :return: 校验通过后的request数据
    #     """
    #     if not re.match('^{.*}$', attr):
    #         raise serializers.ValidationError("输入的请求格式不对，需为json格式")
    #     try:
    #         request_data = json.loads(attr)
    #         if not request_data.get('test') and request_data.get('test').get('request'):
    #             raise serializers.ValidationError("输入的请求格式不对，需为json格式")
    #     except Exception:
    #         raise serializers.ValidationError("输入的请求格式不对，需为json格式")
    #     return attr
    #
    # def validate_include(self, attrs):
    #     """
    #     单字段校验，校验include的数据格式
    #     :param attr: 请求中include数据
    #     :return: 校验通过后的include数据
    #     """
    #     # {"config": 1, "testcases": []}
    #     if not re.match('^{.*}$', attrs):
    #         raise serializers.ValidationError("输入的请求格式不对，需为json格式1")
    #     try:
    #         request_data = json.loads(attrs)
    #     except Exception:
    #         raise serializers.ValidationError("输入的请求格式不对，需为json格式2")
    #
    #     # if not request_data.get('config') and request_data.get('testcases'):
    #     if not ('config' in request_data.keys() and 'testcases' in request_data.keys()):
    #         raise serializers.ValidationError("输入的请求格式不对，需为json格式3")
    #     return attrs


class TestcaseRunSerializer(RunSerializer, serializers.ModelSerializer):
    """
    继承父类BaseSerializer
    """

    class Meta(RunSerializer.Meta):
        """
        继承父类BaseSerializer的子类，指定模型对象
        """
        model = Testcases
