from datetime import datetime

from django.shortcuts import render


def isitnewyear(request):
    now = datetime.now()
    if now.month == 1 and now.day == 1:
        is_new_year = True
    else:
        is_new_year = False

    return render(
        request,
        'is_it_new_year.html',
        {
            'is_new_year': True
        }
    )


def template_view(request):
    fruits = [
        'jabłko',
        'banan',
        'mandarynki'
    ]
    user = {
        'name': 'John',
        'surname': 'Doe',
        'age': 10
    }

    class Cow:
        def __init__(self, name):
            self.name = name

    cow = Cow("Mućka")

    return render(
        request,
        'template.html',
        {
            'fruits': fruits,
            'user': user,
            'cow': cow
        }
    )
