# coding: utf-8
from rest_framework import routers
from . import views

# 创建SimpleRouter路由对象
router = routers.SimpleRouter()

# 路由注册
router.register(r'debugtalks', views.DebugTalksViewSet)
urlpatterns = []
urlpatterns += router.urls
