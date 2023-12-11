# formularz - metoda POST (redirect)
from django.shortcuts import render, redirect, Http404, get_object_or_404

from form_app6.models import Task

TASKS = []


# C z CRUD
def task_create_view(request):
    if request.method == "GET":
        return render(
            request,
            'form_app6/task_form.html',
        )

    if request.method == "POST":
        task = request.POST.get('task')
        if task is not None:
            Task.objects.create(name=task)

        return redirect('form_app6:task_list')


# R (lista) z CRUD
def task_list_view(request):
    return render(
        request,
        'form_app6/task_list.html',
        {
            'tasks': Task.objects.all()
        }
    )


# R (szczegół) z CRUD
def task_detail_view(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    return render(
        request,
        'form_app6/task_detail.html',
        {
            'task': task
        }
    )


# U z CRUD
def task_update_view(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "GET":
        return render(
            request,
            'form_app6/task_update.html',
            {
                'task': task
            }
        )

    if request.method == "POST":
        new_task = request.POST.get('task')
        if new_task is not None:
            task.name = new_task
            task.save()

        return redirect('form_app6:task_list')


# D z CRUD
def task_delete_view(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "GET":
        return render(
            request,
            'form_app6/task_confirm_delete.html',
            {
                'task': task
            }
        )

    elif request.method == "POST":
        data = request.POST
        if 'yes' in data:
            task.delete()

        return redirect('form_app6:task_list')
