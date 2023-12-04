from django.urls import path

from hello.views import hello_view, hello_eva, hello_adam, hello_name, hello_template, hello_template2


urlpatterns = [
    path('', hello_view),
    path('eva/', hello_eva),
    path('adam/', hello_adam),
    path('<str:name>/', hello_name),

    path('template/<str:name>/', hello_template),
    path('template2/<str:name>/', hello_template2),
]