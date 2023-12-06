from django.urls import path

from form_app2.views import task_create_view

app_name = 'form_app2'

urlpatterns = [
    path('', task_create_view, name='create_task')
]