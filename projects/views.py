# Create your views here.


from rest_framework import status, filters
# from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from .serializers import ProjectsModelSerializer, ProjectSerializer
from projects.models import Projects
from rest_framework import viewsets
import logging

log = logging.getLogger('wl')


class ProjectViewSet(viewsets.ModelViewSet):
    """
        list:
        获取项目列表数据

        retrieve:
        获取项目详情数据

        update:
        更新项目信息

        names:
        获取项目名称

        """
    queryset = Projects.objects.all()
    serializer_class = ProjectsModelSerializer

    @action(methods=['GET'], detail=False)
    def names(self, request, *args, **kwargs):
        log.info('ceshi')
        return super().list(request, *args, **kwargs)

