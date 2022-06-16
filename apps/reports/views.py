# coding:utf-8
import json
from django.http import StreamingHttpResponse
from rest_framework import mixins, viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Reports
from . import serializers


class ReportViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    """
    create:
    创建报告数据

    retrieve:
    获取报告详情数据

    delete:
    删除报告信息

    download:
    下载报告

    """
    queryset = Reports.objects.all()
    serializer_class = serializers.ReportsModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        """
        重写父类方法，增加校验报告格式
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        instance = self.get_object()
        try:
            summary = json.loads(instance.summary)
            return Response({
                'id': instance.id,
                'summary': summary
            }, status=status.HTTP_200_OK)
        except Exception:
            return Response({
                'err': '测试报告summary格式有误'
            }, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True)
    def download(self, request, *args, **kwargs):
        """
        下载报告
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        # 1、获取html源码
        instance = self.get_object()
        # 2、将html源码转化为生成器对象
        # byte_data = instance.html.encode('utf-8')
        byte_data = instance.html
        # 3、StreamingHttpResponse对象
        response = StreamingHttpResponse(iter(byte_data))
        # StreamingHttpResponse、HttpResponse、Response，这些['key'] = 'value'，可以添加响应头数据
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = f"attachment; filename*=UTF-8 '' {instance.name + '.html'}"
        return response
