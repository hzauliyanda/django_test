from django.db import models

# Create your models here.
from utils.base_model import BaseModel


class Animal(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.BooleanField()


class Projects(BaseModel):
    name = models.CharField(max_length=50, verbose_name='项目名称', help_text='项目名称')
    leader = models.CharField(max_length=20, verbose_name='项目负责人', help_text='项目负责人')
    is_execute = models.BooleanField(verbose_name='是否启动项目', help_text='是否启动项目', default=True)
    desc = models.TextField(verbose_name='项目描述信息', help_text='项目描述信息', null=True, blank=True, default='')

    class Meta:
        db_table = 'tb_projects'
        verbose_name = '项目表'
        verbose_name_plural = '项目表'
        # ordering=['id']

    # def __str__(self):
    #     print(f'projects({self.name})')
