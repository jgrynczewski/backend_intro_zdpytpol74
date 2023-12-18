from django.shortcuts import render


def contact1(request):
    return render(
        request,
        'forms_app/contact1.html'
    )
