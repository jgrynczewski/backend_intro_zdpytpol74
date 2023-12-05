from django.urls import path

from link_app.views import first_view


urlpatterns = [
    path('first/', first_view)
]