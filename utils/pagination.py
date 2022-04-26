# coding:utf-8

from rest_framework.pagination import PageNumberPagination as _PageNumberPagination


class PageNumberPagination(_PageNumberPagination):
    page_size = 5
    page_query_param = 'page'
    page_query_description = '获取的页码'

    page_size_query_param = 'size'
    page_size_query_description = '每一页数据条数'

    # 当接口uri中传入的size大于当前设置的max_page_size，则按max_page_size中的数据返回数据个数
    max_page_size = 4
    invalid_page_message = '无效页码'

    def get_paginated_response(self, data):
        response = super().get_paginated_response(data)
        response.data['current_num'] = self.page.number
        response.data['max_num'] = self.page.paginator.num_pages
        return response
