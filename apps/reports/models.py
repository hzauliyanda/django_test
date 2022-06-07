# -*- coding: utf-8 -*-
# @Date    : 2022/6/2 下午5:05
# @Author  : Cristiano Ronalda

from django.db import models
from utils.base_model import BaseModel


class Reports(BaseModel):
    """
    id:主键
    name：报告名称
    result：执行结果
    count：用例总数
    success：成功总数
    html：报告HTML源码
    summary：报告详情
    """
    id = models.AutoField(verbose_name='id主键', primary_key=True, help_text='id主键')
    name = models.CharField('报告名称', max_length=200, unique=True, help_text='报告名称')
    result = models.BooleanField('执行结果', default=1, help_text='执行结果')   # 1为成功, 0为失败
    count = models.IntegerField('用例总数', help_text='总用例数')
    success = models.IntegerField('成功总数', help_text='成功总数')
    html = models.TextField('报告HTML源码', help_text='报告HTML源码', null=True, blank=True, default='')
    summary = models.TextField('报告详情', help_text='报告详情', null=True, blank=True, default='')

    class Meta:
        """
        db_table：生成的数据库表名
        verbose_name：管理界面的别名
        """
        db_table = 'tb_reports'
        verbose_name = '测试报告'
        verbose_name_plural = verbose_name

    def __str__(self):
        """
        db_table：生成的数据库表名
        verbose_name：管理界面的别名
        """
        return self.name