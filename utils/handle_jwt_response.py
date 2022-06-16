# -*- coding: utf-8 -*-
# @Date    : 2022/4/26 上午9:09
# @Author  : Cristiano Ronalda
import logging

log = logging.getLogger('wl')


def jwt_response_payload_handler(token, user=None, request=None):
    """
    登录成功后返回token
    :param token:
    :param user:
    :param request:
    :return:
    """
    result_dict = {
        'user_id': user.id,
        'username': user.username,
        'token': token
    }

    log.info(f"用户[{user.username}]登录成功，返回数据为："+str(result_dict))
    return result_dict
