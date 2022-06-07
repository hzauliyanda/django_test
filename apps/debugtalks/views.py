# coding: utf-8
from rest_framework import mixins, viewsets, permissions
from . import serializers
from debugtalks.models import DebugTalks


class DebugTalksViewSet(mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        viewsets.GenericViewSet):
    """
    内置函数视图集，继承ListModelMixin/RetrieveModelMixin/UpdateModelMixin，支持的action如下：
    1、list；
    2、retrieve；
    3、update；
    """
    queryset = DebugTalks.objects.all()
    serializer_class = serializers.DebugTalksModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        """
        根据action动作来调用不同的序列化器类
        :return:
        """
        return serializers.DebugTalksSerializer if self.action == 'retrieve' else self.serializer_class
