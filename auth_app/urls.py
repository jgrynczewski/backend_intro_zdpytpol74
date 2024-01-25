from django.urls import path, include

from auth_app import views

app_name = 'auth_app'

urlpatterns = [
    path('auto/', include('django.contrib.auth.urls')),
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registration/', views.registration_view, name='registration')
]
