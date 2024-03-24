from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.project_list, name = 'project-list'),
    path('tasks/', views.task_status_list, name='task-list'),
    path('update_task_status/', views.update_task_status, name='update_task_status'),

]