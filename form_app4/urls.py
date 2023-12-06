from django.urls import path

from form_app4.views import task_create_view, task_list_view

app_name = 'form_app4'

urlpatterns = [
    path('tasks/create/', task_create_view, name='create_task'),
    path('tasks/', task_list_view, name='task_list'),
]