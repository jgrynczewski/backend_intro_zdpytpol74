# formularz - metoda POST
from django.shortcuts import render

TASKS = []


def task_create_view(request):
    if request.method == "GET":
        return render(
            request,
            'form_app3/task_form.html',
            {
                'tasks': TASKS
            }
        )

    if request.method == "POST":
        task = request.POST.get('task')
        if task is not None:
            TASKS.append(task)

        return render(
            request,
            'form_app3/task_form.html',
            {
                'tasks': TASKS
            }
        )
