from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def index(request):

    # wyświetlamy wszystkich użytkowników
    users = User.objects.all()
    print(users)

    # Tworzenie użytkownika
    # User.objects.create_user(username='adam', password='tajne')

    # uwierzytelnie użytkownika (jeżeli uwierzytelnienie się nie powiedzie metoda authenticate
    # zwraca None, w przeciwnym razie obiekt użytkownika, który się uwierzytelnił)
    user = authenticate(username='adam', password='tajne')
    print(user)

    # zmiana hasła
    # user.set_password('nowe_tajne')
    # user.save()

    # logowanie (uwierzytelnionego użytkownika)
    # if user: # jeżeli użytkownik się uwierzytelnił to:
    #     login(request, user)  # logujemy się (czyli tworzymy dla niego sesję)

    # wylogowanie
    # logout(request)

    # request.user przechowuje aktualnie zalogowanego użytkownik lub jeżeli użytkownik nie jest zalogowany
    # obiket AnonymousUser
    return render(
        request,
        'auth_app/index.html',
        context = {
            'user': request.user
        }
    )


def login_view(request):
    if request.method == "GET":
        return render(
            request,
            'auth_app/login.html'
        )

    elif request.method == "POST":
        data = request.POST

        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect('auth_app:index')

        return redirect('auth_app:login')


def logout_view(request):
    logout(request)

    return redirect('auth_app:login')
