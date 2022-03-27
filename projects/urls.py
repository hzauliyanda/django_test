from django.urls import path
from projects import views

urlpatterns = [
    path('index/', views.ProjectView.as_view())
]
