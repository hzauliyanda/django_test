# log = logging.getLogger('wl')
from datetime import datetime
from django.db.models import Sum
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from configures.models import Configures
from debugtalks.models import DebugTalks
from envs.models import Envs
from interfaces.models import Interfaces
from projects.models import Projects
from reports.models import Reports
from testcases.models import Testcases
from testsuites.models import Testsuits


class SummaryViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        查询项目下的接口信息
        :param request:
        :param args: 路径参数pk
        :param kwargs:
        :return:
        """
        user, statistics = {}, {}
        result = {}
        user['username'] = request.user.username
        user['role'] = "普通用户"
        if request.user.is_superuser:
            user['role'] = "管理员"
        user['date_joined'] = ''
        user['last_login'] = ''
        if request.user.date_joined is not None:
            user['date_joined'] = datetime.strftime(request.user.date_joined, "%Y-%m-%d %H:%M:%S")
        if request.user.last_login is not None:
            user['last_login'] = datetime.strftime(request.user.last_login, "%Y-%m-%d %H:%M:%S")
        # result.data = result.data.get('interfaces')
        result['user'] = user
        statistics['projects_count'] = Projects.objects.count()
        statistics['interfaces_count'] = Interfaces.objects.all().count()
        statistics['testcases_count'] = Testcases.objects.all().count()
        statistics['testsuits_count'] = Testsuits.objects.all().count()
        statistics['configures_count'] = Configures.objects.all().count()
        statistics['envs_count'] = Envs.objects.all().count()
        statistics['debug_talks_count'] = DebugTalks.objects.all().count()
        statistics['reports_count'] = Reports.objects.all().count()
        count_num = Reports.objects.aggregate(count_sum=Sum('count'))['count_sum']
        success_num = Reports.objects.aggregate(success_sum=Sum('success'))['success_sum']
        statistics['success_rate'] = 0
        if count_num is not None and success_num is not None:
            statistics['success_rate'] = int(round(success_num / count_num, 2) * 100)
        statistics['fail_rate'] = 100 - statistics['success_rate']
        result['user'] = user
        result['statistics'] = statistics
        return Response(result, status=200)
