from django.urls import path

from cookies_app import views

app_name = 'cookies_app'


urlpatterns = [
    path('set_cookies/', views.set_cookies, name='set_cookies'),
    path('get_cookies/', views.get_cookies, name='get_cookies'),
    path('delete_cookies/', views.delete_cookies, name='delete_cookies')
]
