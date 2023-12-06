from django.urls import path

from form_app1.views import task_create_view

app_name = 'form_app1'

urlpatterns = [
    path('', task_create_view, name='create_task')
]