# Create your views here.
from django.http import HttpResponse
from django.views.generic.base import View
from projects.models import Projects
from django.db import models


class ProjectView(View):

    def get(self, request):

        # 创建（C）
        # Projects.objects.create(name='道路项目',leader='金凤')
        # Projects.objects.create(name='亚运会项目1',leader='会见1')
        # Projects.objects.create(name='亚运会项目2',leader='会见2')
        # Projects.objects.create(name='亚运会项目3',leader='会见3')

        # 读取（R）
        obj=Projects.objects.filter(id=1)
        print(obj.name)
        return HttpResponse('数据写入成功')