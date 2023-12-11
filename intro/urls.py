"""
URL configuration for intro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', include('hello.urls')),
    path('template/', include('template_app.urls')),
    path('link/', include('link_app.urls')),
    path('inheritance/', include('inheritance_app.urls')),
    path('form1/', include('form_app1.urls')),
    path('form2/', include('form_app2.urls')),
    path('form3/', include('form_app3.urls')),
    path('form4/', include('form_app4.urls')),
    path('form5/', include('form_app5.urls')),
    path('relation/', include('relation_app.urls')),
    path('form6/', include('form_app6.urls')),

]
