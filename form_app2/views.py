# formularz - metoda POST
from django.shortcuts import render

TASKS = []


def task_create_view(request):
    task = request.POST.get('task')
    if task is not None:
        TASKS.append(task)

    return render(
        request,
        'form_app2/task_form.html',
        {
            'tasks': TASKS
        }
    )
