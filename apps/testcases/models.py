# -*- coding: utf-8 -*-
# @Date    : 2022/6/2 下午5:05
# @Author  : Cristiano Ronalda

from django.db import models
from utils.base_model import BaseModel


class Testcases(BaseModel):
    """
    id:主键
    name：用例名称
    interface：外键，所属接口
    include：用例执行前置顺序
    author：编写人员
    request：请求信息
    """
    id = models.AutoField(verbose_name='id主键', primary_key=True, help_text='id主键')
    name = models.CharField('用例名称', max_length=50, unique=True, help_text='用例名称')
    interface = models.ForeignKey('interfaces.Interfaces', on_delete=models.CASCADE,
                                  help_text='所属接口')
    include = models.TextField('前置', null=True, help_text='用例执行前置顺序')
    author = models.CharField('编写人员', max_length=50, help_text='编写人员')
    request = models.TextField('请求信息', help_text='请求信息')

    class Meta:
        """
        db_table：生成的数据库表名
        verbose_name：管理界面的别名
        """
        db_table = 'tb_testcases'
        verbose_name = '用例信息'
        verbose_name_plural = verbose_name
        ordering = ('id',)

    def __str__(self):
        """
        db_table：生成的数据库表名
        verbose_name：管理界面的别名
        """
        return self.name