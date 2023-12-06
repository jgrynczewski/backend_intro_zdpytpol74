# formularz - metoda POST (redirect)
from django.shortcuts import render, redirect

TASKS = []


def task_create_view(request):
    if request.method == "GET":
        return render(
            request,
            'form_app4/task_form.html',
        )

    if request.method == "POST":
        task = request.POST.get('task')
        if task is not None:
            TASKS.append(task)

        return redirect('form_app4:task_list')


def task_list_view(request):
    return render(
        request,
        'form_app4/task_list.html',
        {
            'tasks': TASKS
        }
    )
