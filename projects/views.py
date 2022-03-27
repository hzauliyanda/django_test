# Create your views here.
from django.http import HttpResponse
from django.views.generic.base import View


class ProjectView(View):

    def get(self, request):
        return HttpResponse('获取项目信息')
