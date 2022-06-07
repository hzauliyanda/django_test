# -*- coding: utf-8 -*-
# @Date    : 2022/6/2 下午2:05
# @Author  : Cristiano Ronalda
from rest_framework.decorators import action


class NameMixin:

    @action(methods=['GET'], detail=False)
    def names(self, request, *args, **kwargs):
        """
        自定义action动作names
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        response = super().list(request, *args, **kwargs)
        return response

    def paginate_queryset(self, queryset):
        """
        names action禁用分页功能
        :param queryset:
        :return:
        """
        if self.action == 'names':
            return
        else:
            return super().paginate_queryset(queryset)

    def filter_queryset(self, queryset):
        """
        names action禁用过滤功能
        :param queryset:
        :return:
        """
        if self.action == 'names':
            return self.queryset
        else:
            return super().filter_queryset(queryset)
