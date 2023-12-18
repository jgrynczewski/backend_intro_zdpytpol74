from django.urls import path
from django.views.generic import TemplateView

from views_app import views

app_name = "views_app"


urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('hello2/', views.HelloView.as_view(), name='hello2'),

    # Template View
    path('template/hello/', views.hello_template, name='hello-template'),
    path('template/hello2/', views.HelloClassView.as_view(), name='hello-template2'),
    path('template/hello3/', views.HelloGenericView.as_view(), name='hello-template3'),
    path(
        'template/hello4/',
        TemplateView.as_view(template_name='views_app/hello.html'),
        name='hello-template4'
    ),
    path('template/hello5/', views.HelloGenericView2.as_view(), name='hello-template5')

    # DetailView

]
