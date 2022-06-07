# -*- coding: utf-8 -*-
# @Date    : 2022/6/2 下午5:05
# @Author  : Cristiano Ronalda

from django.db import models
from utils.base_model import BaseModel


class DebugTalks(BaseModel):
    """
    DebugTalks模型类
    id：主键
    name：debugtalk文件名称
    debugtalk：具体的代码内容
    project：关联项目id
    """
    id = models.AutoField(verbose_name='id主键', primary_key=True, help_text='id主键')
    name = models.CharField('debugtalk文件名称', max_length=200, default='debugtalk.py', help_text='debugtalk文件名称')
    debugtalk = models.TextField(null=True, default='#debugtalk.py', help_text='debugtalk.py文件')
    project = models.OneToOneField('projects.Projects', on_delete=models.CASCADE,
                                   related_name='debugtalks', help_text='所属项目')

    class Meta:
        """
        db_table：生成的数据库表名
        verbose_name：管理界面的别名
        """
        db_table = 'tb_debugtalks'
        verbose_name = 'debugtalk.py文件'
        verbose_name_plural = verbose_name

    def __str__(self):
        """
        StringRelatedField，字段将被序列化为关联对象的字符串表示方式（即__str__方法的返回值）
        :return:
        """
        return self.name
