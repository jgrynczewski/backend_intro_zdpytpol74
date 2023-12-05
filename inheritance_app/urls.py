from django.urls import path

from inheritance_app.views import first_view

app_name = "inheritance_app"

urlpatterns = [
    path('first/', first_view, name='first_name'),
]