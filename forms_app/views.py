from django.shortcuts import render, redirect

from forms_app.models import Message


def contact1(request):

    if request.method == "POST":
        data = request.POST
        Message.objects.create(
            name=data.get("name"),
            email=data.get("email"),
            category=data.get("category"),
            subject=data.get("subject"),
            body=data.get("body"),
            date=data.get("date"),
            time=data.get("time")
        )

        return redirect('forms_app:contact1')

    return render(
        request,
        'forms_app/contact1.html'
    )


def contact2(request):
    return render(
        request,
        'forms_app/contact2.html',
    )