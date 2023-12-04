from django.urls import path

from template_app.views import isitnewyear

urlpatterns = [
    path('isitnewyear/', isitnewyear),
]