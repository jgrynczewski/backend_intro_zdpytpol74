# formularz - metoda POST (redirect)
from django.shortcuts import render, redirect, Http404

TASKS = []


# C z CRUD
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


# R (lista) z CRUD
def task_list_view(request):
    return render(
        request,
        'form_app4/task_list.html',
        {
            'tasks': TASKS
        }
    )


# R (szczegół) z CRUD
def task_detail_view(request, task_id):
    if task_id > len(TASKS):
        raise Http404()

    task = TASKS[task_id-1]
    return render(
        request,
        'form_app4/task_detail.html',
        {
            'task_id': task_id,
            'task': task
        }
    )


# U z CRUD
def task_update_view(request, task_id):
    if task_id > len(TASKS):
        raise Http404()

    if request.method == "GET":
        task = TASKS[task_id - 1]

        return render(
            request,
            'form_app4/task_update.html',
            {
                'task_id': task_id,
                'task': task
            }
        )

    if request.method == "POST":
        new_task = request.POST.get('task')
        if new_task is not None:
            TASKS[task_id-1] = new_task

        return redirect('form_app4:task_list')
