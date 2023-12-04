from django.urls import path

from hello.views import hello_view


urlpatterns = [
    path('', hello_view),
]