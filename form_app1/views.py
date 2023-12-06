# formularz - metoda GET
from django.shortcuts import render

TASKS = []


def task_create_view(request):
    task = request.GET.get('task')
    if task is not None:
        TASKS.append(task)

    return render(
        request,
        'form_app1/task_form.html',
        {
            'tasks': TASKS
        }
    )