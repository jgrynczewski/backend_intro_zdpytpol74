from django.urls import path

from template_app.views import isitnewyear, template_view

urlpatterns = [
    path('isitnewyear/', isitnewyear),
    path('', template_view),
]