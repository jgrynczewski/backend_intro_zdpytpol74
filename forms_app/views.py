from django.shortcuts import render, redirect

from forms_app.models import Message
from forms_app.forms import ContactForm, MessageForm


# HTML Form
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


# Django Form
def contact2(request):
    if request.method == "POST":
        form = ContactForm(request.POST)  # bound Django form
        if form.is_valid():
            data = form.cleaned_data
            Message.objects.create(
                name=data.get("name"),
                email=data.get("email"),
                category=data.get("category"),
                subject=data.get("subject"),
                body=data.get("body"),
                date=data.get("date"),
                time=data.get("time")
            )

            return redirect('forms_app:contact2')

        return render(
            request,
            'forms_app/contact2.html',
            {
                'form': form
            }
        )

    form = ContactForm()  # unbound Django form

    return render(
        request,
        'forms_app/contact2.html',
        {
            'form': form
        }
    )


# Model Form
def contact3(request):
    if request.method == "POST":
        form = MessageForm(request.POST)  # unbound Django model form
        if form.is_valid():
            form.save()

        return render(
            request,
            'forms_app/contact2.html',
            {
                'form': form
            }
        )

    form = MessageForm()  # unbound Django model form
    return render(
        request,
        'forms_app/contact3.html',
        {
            'form': form
        }
    )
