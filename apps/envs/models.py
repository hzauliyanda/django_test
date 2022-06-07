# -*- coding: utf-8 -*-
# @Date    : 2022/6/2 下午5:05
# @Author  : Cristiano Ronalda

from django.db import models
from utils.base_model import BaseModel


class Envs(BaseModel):
    """
    id:主键
    name：环境名称
    base_url：请求base url
    desc：简要描述
    """
    id = models.AutoField(verbose_name='id主键', primary_key=True, help_text='id主键')
    name = models.CharField(verbose_name='环境名称', max_length=200, unique=True, help_text='环境名称')
    base_url = models.URLField(verbose_name='请求base url', max_length=200, help_text='请求base url')
    desc = models.CharField(verbose_name='简要描述', max_length=200, help_text='简要描述')

    class Meta:
        """
        db_table：生成的数据库表名
        verbose_name：管理界面的别名
        """
        db_table = 'tb_envs'
        verbose_name = '环境信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        """
        StringRelatedField，字段将被序列化为关联对象的字符串表示方式（即__str__方法的返回值）
        :return:
        """
        return self.name
