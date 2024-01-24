from django.shortcuts import render, HttpResponse


# Create your views here.
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
