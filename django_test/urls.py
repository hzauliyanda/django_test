"""django_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.documentation import include_docs_urls
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_jwt.views import obtain_jwt_token

schema_view = get_schema_view(
    openapi.Info(title="Lemon API接口文档平台",  # 必传
                 default_version='v1',  # 必传
                 description="这是一个美轮美奂的接口文档",
                 terms_of_service="http://api.keyou.site",
                 contact=openapi.Contact(email="keyou100@qq.com"),
                 license=openapi.License(name="BSD License"), ),
    public=True
)
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('parent/', include('projects.urls'))
    path('', include('projects.urls')),
    path('docs/', include_docs_urls(title='test接口文档', description='哈哈哈哈哈哈，这是哥的第一个接口文档')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # 在全局路由表中添加rest_framework.urls子路由
    # a.rest_framework.urls提供了登录和登出功能（返回的是一个HTML页面，并不是接口）
    # path('api/', include('rest_framework.urls')),

    path('user/', include('users.urls')),
]
