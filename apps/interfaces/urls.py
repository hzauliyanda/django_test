from django.urls import path, include
from rest_framework import routers
from . import views


# 创建SimpleRouter路由对象
router = routers.SimpleRouter()

# 路由注册
router.register(r'interfaces', views.InterfacesViewSet)
urlpatterns = [
]
urlpatterns += router.urls
