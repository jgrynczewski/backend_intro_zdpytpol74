from django.urls import path

from form_app3.views import task_create_view

app_name = 'form_app3'

urlpatterns = [
    path('', task_create_view, name='create_task')
]