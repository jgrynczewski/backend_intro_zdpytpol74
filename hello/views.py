from django.shortcuts import HttpResponse, render


def hello_view(request):
    return HttpResponse("Hello, world!")


def hello_eva(request):
    return HttpResponse("Hello, Eva!")


def hello_adam(request):
    return HttpResponse("Hello, Adam!")


def hello_name(request, name):
    return HttpResponse(f"Hello, {name}! Nice to see you.")


def hello_template(request, name):
    return HttpResponse(f"""
        <!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>Title</title>
            </head>
            <body>
                <h1>Hello, {name}!</h1>
            </body>
        </html>
    """)


def hello_template2(request, name):
    return render(
        request,
        'name_template.html',
        context={
            'name': name
        }
    )
