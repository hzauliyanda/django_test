from django.urls import path, include
from rest_framework import routers
from . import views

# 创建SimpleRouter路由对象
router = routers.SimpleRouter()

# 路由注册
router.register(r'envs', views.EnvsViewSet)
urlpatterns = [
]
urlpatterns += router.urls
