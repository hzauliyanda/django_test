# coding:utf-8
"""
序列化器，子应用中创建serializers.py文件
"""
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from interfaces.models import Interfaces
from projects.models import Projects


def is_contains_keyword(value):
    if '项目' not in value:
        raise serializers.ValidationError("项目名称中必须包含'项目'关键字")


class ProjectSerializer(serializers.Serializer):
    name = serializers.CharField(label='项目名称', help_text='项目名称', max_length=20, min_length=5,
                                 error_messages={"min_length": "最短不能少于5位"},
                                 validators=[UniqueValidator(queryset=Projects.objects.all(), message="项目名称不能重复"),
                                             is_contains_keyword])
    leader = serializers.CharField(label='项目负责人', help_text='项目负责人')
    # leader=serializers.CharField(label='',help_text='',default='小芳')
    # leader=serializers.CharField(label='',help_text='',allow_null=True)
    # leader=serializers.CharField(label='',help_text='',allow_blank=True)
    is_execute = serializers.BooleanField(write_only=True)
    # read_only--只输出不校验
    update_time = serializers.DateTimeField(read_only=True)

    # 关联字段
    # interfaces_set = serializers.PrimaryKeyRelatedField(label='项目所属接口id', help_text='项目所属接口id', many=True ,
    #                                                     queryset=Interfaces.objects.all(), write_only=True)
    # interfaces_set = serializers.SlugRelatedField(slug_field='name', many=True, queryset=Interfaces.objects.all())

    def validate_name(self, attr: str):
        if not attr.startswith('项目'):
            raise serializers.ValidationError('项目名称必须得以“项目”结尾')
        return attr

    # 1、可以在序列化器类中对多个字段进行联合校验
    # 2、使用固定的validate方法，会接收上面校验通过之后的字典数据
    # 3、当所有字段定义时添加的校验规则都通过，且每个字段的单字段校验方法通过的情况下，才会调用validate
    def validate(self, attrs: dict):
        if len(attrs.get('leader')) <= 4 or not attrs.get('is_execute'):
            raise serializers.ValidationError('项目负责人名称长度不能少于4位或者is_execute参数为False')
        return attrs

    def create(self, validated_data):
        project_obj = Projects.objects.create(**validated_data)
        return project_obj

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name') or instance.name
        instance.leader = validated_data.get('leader') or instance.leader
        instance.save()
        return instance


class ProjectsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = "__all__"
        # fields = ('id', 'name', 'leader')
        extra_kwargs = {
            'leader': {
                'label': '负责人',
                'max_length': 15,
                'min_length': 2,
                # 'read_only': True
                # 'validators': []
            },
            'name': {
                'min_length': 5
            }
        }
