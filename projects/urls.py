from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register(r'projects', views.ProjectViewSet)
urlpatterns = [
    path('', include(router.urls))
    # path('index/', views.ProjectView.as_view()),
    # path('projects/', views.ProjectsView.as_view()),
    # path('projects/<int:pk>', views.ProjectDetailView.as_view())
    # path('projects/', views.ProjectViewSet.as_view({
    #     'get': 'list',
    #     'post': 'create'
    # })),
    # path('projects/<int:pk>', views.ProjectViewSet.as_view({
    #     'get': 'retrieve',
    #     'put': 'update',
    #     'patch': 'partial_update',
    #     'delete': 'destroy'
    # }))

]
