from django.urls import path

from hello.views import hello_view, hello_eva, hello_adam, hello_name


urlpatterns = [
    path('', hello_view),
    path('eva/', hello_eva),
    path('adam/', hello_adam),
    path('<str:name>/', hello_name),
]