from django.urls import path

from cookies_app import views

app_name = 'cookies_app'


urlpatterns = [
    # ciasteczka
    path('set_cookies/', views.set_cookies, name='set_cookies'),
    path('get_cookies/', views.get_cookies, name='get_cookies'),
    path('delete_cookies/', views.delete_cookies, name='delete_cookies'),

    # sesja
    path('set_session/', views.set_session, name='set_session'),
    path('get_session/', views.get_session, name='get_session'),
    path('delete_session/', views.delete_session, name='delete_session'),
]
