from django.urls import path

from forms_app import views

app_name = 'forms_app'

urlpatterns = [
    path('contact1/', views.contact1, name='contact1')
]