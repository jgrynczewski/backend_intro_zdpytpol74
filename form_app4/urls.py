from django.urls import path

from form_app4 import views

app_name = 'form_app4'

urlpatterns = [
    # C z CRUD
    path('tasks/create/', views.task_create_view, name='create_task'),
    # R z CRUD (lista)
    path('tasks/', views.task_list_view, name='task_list'),

    # R z CRUD (szczegół)
    path('tasks/<int:task_id>/', views.task_detail_view, name='task_detail'),
    # U z CRUD
    path('tasks/<int:task_id>/update/', views.task_update_view, name='task_update'),
]
