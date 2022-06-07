# -*- coding: utf-8 -*-
# @Date    : 2022/6/2 下午5:05
# @Author  : Cristiano Ronalda

from django.db import models
from utils.base_model import BaseModel


class Interfaces(BaseModel):
    """
    id:主键
    name：接口名称
    tester：测试人员
    project：关联项目id
    desc：简要描述
    """
    id = models.AutoField(verbose_name='id主键', primary_key=True, help_text='id主键')
    name = models.CharField(max_length=200, verbose_name='接口名称', help_text='接口名称', unique=True)
    tester = models.CharField(max_length=50, verbose_name='测试人员', help_text='测试人员')
    project = models.ForeignKey('projects.Projects', on_delete=models.CASCADE, related_name='interfaces',
                                verbose_name='所属项目', help_text='所属项目')
    desc = models.CharField('简要描述', max_length=200, null=True, blank=True, help_text='简要描述')

    class Meta:
        """
        db_table：生成的数据库表名
        verbose_name：管理界面的别名
        """
        db_table = 'tb_interfaces'
        verbose_name = '接口信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        """
        StringRelatedField，字段将被序列化为关联对象的字符串表示方式（即__str__方法的返回值）
        :return:
        """
        return self.name
