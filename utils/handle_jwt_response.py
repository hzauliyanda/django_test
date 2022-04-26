# -*- coding: utf-8 -*-
# @Date    : 2022/4/26 上午9:09
# @Author  : Cristiano Ronalda


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'user_id': user.id,
        'username': user.username,
        'token': token
    }
