from django.core import paginator
from django.db.models import manager
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import TaskList
from todolist_app.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import auth

# Create your views here.


@login_required
def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.manage = request.user
            instance.save()
            messages.success(request, "New Task Added")
        return redirect('todolist')
    else:
        task_list = TaskList.objects.filter(manage=request.user)
        paginator = Paginator(task_list, 10)
        page = request.GET.get('pg')
        # get_page use for the  getting page number
        task_list = paginator.get_page(page)
        return render(request, 'todolist.html', {'task_list': task_list})


@login_required
def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.manage == request.user:
        task.delete()
    else:
        messages.success(request, ("Restricted! You can not update"))
    return redirect('todolist')


@login_required
def edit_task(request, task_id):
    if request.method == "POST":
        task = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
        messages.success(request, "New Task Added")
        return redirect('todolist')
    else:
        task_object = TaskList.objects.get(pk=task_id)
        return render(request, 'edit.html', {'task_object': task_object})


@login_required
def complete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.manage == request.user:
        task.done = True
        task.save()
    else:
        messages.success(request, ("Restricted! You can not update"))

    return redirect('todolist')


@login_required
def pending_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = False
    task.save()

    return redirect('todolist')


def index(request):
    context = {
        'index_txt': "Welcome to the new website"
    }
    return render(request, 'index.html', context)


# def stool(request):
#     context = {
#         'stool_txt': "Welcome to the new website"
#     }
#     return render(request, 'stool.html', context)


def contact(request):
    context = {
        'contact_txt': "contact with to todolist app! with"
    }
    return render(request, 'contact.html', context)


def aboutus(request):
    context = {
        'aboutus_txt': "contact withus for query to todolist app! with"
    }
    return render(request, 'aboutus.html', context)


def about(request):
    context = {
        'about_txt': "contact withus for query to todolist app! with"
    }
    return render(request, 'aboutus.html', context)
