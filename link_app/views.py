from django.shortcuts import render


# Create your views here.
def first_view(request):
    return render(
        request,
        'first.html'
    )
