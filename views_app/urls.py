from django.urls import path

from views_app import views

app_name = "views_app"


urlpatterns = [
    path('hello/', views.hello, name='hello'),
]
