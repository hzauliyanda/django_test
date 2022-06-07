# -*- coding: utf-8 -*-
# @Date    : 2022/6/2 下午5:05
# @Author  : Cristiano Ronalda

from django.db import models
from utils.base_model import BaseModel


class Projects(BaseModel):
    """
    id:主键
    name：项目名称
    leader：项目负责人
    tester：项目测试人员
    programmer：开发人员
    publish_app：发布应用
    desc：简要描述
    """
    id = models.AutoField(verbose_name='id主键', primary_key=True, help_text='id主键')
    name = models.CharField(max_length=200, verbose_name='项目名称', help_text='项目名称', unique=True)
    leader = models.CharField(max_length=50, verbose_name='项目负责人', help_text='项目负责人')
    tester = models.CharField('测试人员', max_length=50, help_text='项目测试人员')
    programmer = models.CharField('开发人员', max_length=50, help_text='开发人员')
    publish_app = models.CharField('发布应用', max_length=100, help_text='发布应用')
    desc = models.CharField('简要描述', max_length=200, null=True, blank=True, default='', help_text='简要描述')

    class Meta:
        """
        db_table：生成的数据库表名
        verbose_name：管理界面的别名
        """
        db_table = 'tb_projects'
        verbose_name = '项目信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        """
        StringRelatedField，字段将被序列化为关联对象的字符串表示方式（即__str__方法的返回值）
        :return:
        """
        return self.name
