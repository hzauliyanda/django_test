# coding:utf-8
from rest_framework import serializers
from .models import Reports


class ReportsModelSerializer(serializers.ModelSerializer):
    """
    定义项目模型序列化器类
    """
    class Meta:
        """
        model：指定序列化模型类
        exclude：指定模型类中update_time不需要转化为序列化器字段
        read_only_fields：这些字段只输出
        extra_kwargs：
            create_time只输出，并且格式化
            name：只输出
            summary/html：只输入
        """
        model = Reports
        exclude = ('update_time',)
        read_only_fields = ('name', 'count', 'result', 'success')
        extra_kwargs = {
            "create_time": {
                "read_only": True,
                "format": "%Y年%m月%d日 %H:%M:%S"
            },
            "name": {
                "read_only": True,
            },
            "html": {
                "write_only": True
            },
            "summary": {
                "write_only": True
            }
        }

    def to_representation(self, instance):
        """
        重写父类方法，增加结果值
        :param instance:
        :return:
        """
        data = super().to_representation(instance)
        data['result'] = '成功' if data.get('result') else '失败'
        return data
