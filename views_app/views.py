from django.shortcuts import render, HttpResponse, get_object_or_404

from django import views
from django.views.generic import TemplateView, DetailView

from views_app.models import Person


# function-based view
def hello(request):
    return HttpResponse("Hello, world!")


# class-based view
class HelloView(views.View):
    def get(self, request):
        return HttpResponse("Hello, world!")


# A jak z wyświetlaniem szablonów ?

# function-based view
def hello_template(request):
    return render(
        request,
        'views_app/hello.html'
    )


# class-based view
class HelloClassView(views.View):
    def get(self, request):
        return render(
            request,
            'views_app/hello.html'
        )


# generic view
class HelloGenericView(TemplateView):
    template_name = 'views_app/hello.html'


# A co jeżeli chcemy przekazać coś do kontekstu szablonu używając widoku generycznego ?
class HelloGenericView2(TemplateView):
    template_name = 'views_app/hello2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Uzupełniamy kontekst szablonu
        context['name'] = "Eva"

        return context

# Widok detalu (R z CRUD)


# function-based view
def person_detail(request, person_id):
    person = get_object_or_404(Person, id=person_id)

    return render(
        request,
        'views_app/person_detail.html',
        {
            "person": person
        }
    )


# class-based view
class PersonView(views.View):
    def get(self, request, person_id):
        person = get_object_or_404(Person, id=person_id)

        return render(
            request,
            'views_app/person_detail.html',
            {
                "person": person
            }
        )


class PersonDetailView(DetailView):
    model = Person
