# coding:utf-8

from rest_framework.pagination import PageNumberPagination as _PageNumberPagination
import logging

log = logging.getLogger('wl')


class PageNumberPagination(_PageNumberPagination):
    """
    重写父类，指定分页信息
    """
    page_size = 5
    page_query_param = 'page'
    page_query_description = '获取的页码'

    page_size_query_param = 'size'
    page_size_query_description = '每一页数据条数'

    # 当接口uri中传入的size大于当前设置的max_page_size，则按max_page_size中的数据返回数据个数
    max_page_size = 50
    invalid_page_message = '无效页码'

    def get_paginated_response(self, data):
        """
        重写父类方法，增加返回总数量和当前页码
        :param data:
        :return:
        """
        response = super().get_paginated_response(data)
        response.data['current_num'] = self.page.number
        response.data['max_num'] = self.page.paginator.num_pages
        log.info(f"分页返回数据为：{str(response)}")
        return response
