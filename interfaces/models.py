from django.db import models

# Create your models here.
from utils.base_model import BaseModel


class Interfaces(BaseModel):
    name = models.CharField(max_length=20, verbose_name='接口名称', help_text='接口名称', unique=True)
    tester = models.CharField(max_length=10, verbose_name='测试人员', help_text='测试人员')
    projects = models.ForeignKey('projects.Projects', on_delete=models.CASCADE, verbose_name='所属项目', help_text='所属项目')

    class Meta:
        db_table = 'tb_interfaces'
        verbose_name = '接口表'
        verbose_name_plural = '接口表'

    def __str__(self):
        return f"Interfaces({self.name})"
