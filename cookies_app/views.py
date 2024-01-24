from django.shortcuts import render, HttpResponse


# ciasteczka
def set_cookies(request):
    res = HttpResponse("OK")

    # żadanie zapisania ciasteczek (w odpowiedzi)
    res.set_cookie("ciasteczko1", 5)
    # max_age w sekundach
    res.set_cookie("ciasteczko2", 10, max_age=15)

    return res


def get_cookies(request):
    # odczyt ciasteczek dołączonych do zapytania
    cookies = request.COOKIES

    return render(
        request,
        'cookies_app/cookies.html',
        {
            'cookies': cookies
        }
    )


def delete_cookies(request):
    res = HttpResponse("Usunięto ciasteczko1")
    res.delete_cookie("ciasteczko1")

    return res


# sesja
def set_session(request):
    request.session['animal'] = 'krowa'
    return HttpResponse("Dodano do sesji klucz animal z wartością krowa")


def get_session(request):
    # odczyt danych sesji
    session = request.session

    return render(
        request,
        'cookies_app/session.html',
        {
            'session': session
        }
    )


def delete_session(request):
    if 'animal' in request.session:
        del request.session['animal']

    return HttpResponse("Usunięto z sesji klucz animal")
