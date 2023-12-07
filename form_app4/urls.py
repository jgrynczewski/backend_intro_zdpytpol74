from django.urls import path

from form_app4.views import task_create_view, task_list_view, task_detail_view

app_name = 'form_app4'

urlpatterns = [
    # C z CRUD
    path('tasks/create/', task_create_view, name='create_task'),
    # R z CRUD (lista)
    path('tasks/', task_list_view, name='task_list'),

    # R z CRUD (szczegół)
    path('tasks/<int:task_id>/', task_detail_view, name='task_detail')
]
