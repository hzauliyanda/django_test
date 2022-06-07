# coding:utf-8
from rest_framework import serializers
from .models import Interfaces
from projects.models import Projects
from testcases.models import Testcases
from configures.models import Configures


class InterfacesModelSerializer(serializers.ModelSerializer):
    """
    定义接口模型序列化器类
    project为项目名称
    project_id为项目主键
    """
    project = serializers.StringRelatedField(label='所属项目名称', help_text='所属项目名称')
    project_id = serializers.PrimaryKeyRelatedField(label='所属项目id', help_text='所属项目id', queryset=Projects.objects.all())

    class Meta:
        """
        model：指定序列化模型类
        exclude：指定模型类中update_time不需要转化为序列化器字段
        extra_kwargs：create_time只输出，并且格式化
        """
        model = Interfaces
        exclude = ('update_time',)
        extra_kwargs = {
            'create_time': {
                'read_only': True,
                'format': '%Y%m%d %H%M%S'
            }
        }

    def to_internal_value(self, data):
        """
        重写父类方法，更新project为模型类对象，反序列化时需要project字段
        :param data:
        :return:
        """
        result = super().to_internal_value(data)
        result['project'] = result.pop('project_id')
        return result


class TestcasesNamesModelSerializer(serializers.ModelSerializer):
    """
    序列化器类，生成序列化器字段时只生成id和name
    """
    class Meta:
        model = Testcases
        fields = ('id', 'name')


class TestcasesInterfacesModelSerializer(serializers.ModelSerializer):
    """
    1、testcases_set为通过父表获取从表数据，默认需要使用从表模型类名小写_set，如果从表定义字段时指定类related_name，那么就用这个指定的名字
    2、又把序列化器TestcasesNamesModelSerializer输出的数据包了一层
     输出实例：{
    "testcases_set": [{"id": 1,
            "name": "登录接口-正向用例"}]
        }
    """
    testcases_set = TestcasesNamesModelSerializer(label='接口所属用例信息', help_text='接口所属用例信息', many=True, read_only=True)

    class Meta:
        model = Interfaces
        fields = ('testcases_set',)


class ConfiguresNamesModelSerrializer(serializers.ModelSerializer):
    """
    序列化器类，生成序列化器字段时只生成id和name
    """
    class Meta:
        model = Configures
        fields = ('id', 'name')


class ConfiguresInterfacesModelSerializer(serializers.ModelSerializer):
    """
    又把序列化器ConfiguresNamesModelSerrializer输出的数据包了一层
    输出实例：{
            "configures": [{
                    "id": 1,
                    "name": "登录接口配置_自动化测试平台项目"
                }]
                }
    """
    configures = ConfiguresNamesModelSerrializer(label='接口所属配置信息', help_text='接口所属配置信息', many=True,
                                                 read_only=True)

    class Meta:
        model = Interfaces
        fields = ('configures',)
