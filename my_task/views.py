from datetime import datetime, timedelta
from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import redirect
from django.core.paginator import EmptyPage
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger

from .models import Task

# Pagination Option.
ITEMS_PER_PAGE = 50


def index(request):
    """
    """
    # Getting all tasks due today and tomorrow.
    tasks_due_today_and_tomorrow = Task.objects.filter(
        time_due__date__lte=(datetime.now().date() + timedelta(days=1)),
        time_due__date__gte=datetime.now().date(),
        status=Task.TASK_NOT_COMPLETED
    ).order_by(
        '-id'
    )
    count_due_today_and_tomorrow = tasks_due_today_and_tomorrow.count()
    paginator = Paginator(tasks_due_today_and_tomorrow, ITEMS_PER_PAGE)
    page = request.GET.get('page')
    try:
        due_today_and_tomorrow = paginator.page(page)
    except PageNotAnInteger:
        # Default to the first page.
        due_today_and_tomorrow = paginator.page(1)
    except EmptyPage:
        # Default to last page
        due_today_and_tomorrow = paginator.page(paginator.num_pages)

    # Getting tasks completed.
    tasks_completed_list = Task.objects.filter(
        status=Task.TASK_COMPLETED
    )
    count_tasks_completed = tasks_completed_list.count()
    paginator = Paginator(tasks_completed_list, ITEMS_PER_PAGE)
    page = request.GET.get('page')
    try:
        tasks_completed = paginator.page(page)
    except PageNotAnInteger:
        # Default to the first page.
        tasks_completed = paginator.page(1)
    except EmptyPage:
        # Default to last page
        tasks_completed = paginator.page(paginator.num_pages)

    # Getting all tasks overdue.
    tasks_overdue = Task.objects.filter(
        time_due__lt=(datetime.now()),
        status=Task.TASK_NOT_COMPLETED
    )
    count_overdue = tasks_overdue.count()
    paginator = Paginator(tasks_overdue, ITEMS_PER_PAGE)
    page = request.GET.get('page')
    try:
        over_due = paginator.page(page)
    except PageNotAnInteger:
        # Default to the first page.
        over_due = paginator.page(1)
    except EmptyPage:
        # Default to last page
        over_due = paginator.page(paginator.num_pages)

    # Getting all tasks.
    tasks_all_list = Task.objects.all()
    count_tasks_all = tasks_all_list.count()
    paginator = Paginator(tasks_all_list, ITEMS_PER_PAGE)
    page = request.GET.get('page')
    try:
        tasks_all = paginator.page(page)
    except PageNotAnInteger:
        # Default to the first page.
        tasks_all = paginator.page(1)
    except EmptyPage:
        # Default to last page
        tasks_all = paginator.page(paginator.num_pages)

    # Check whether the user wants to add a new task.
    if request.POST.get("add_new_task"):
        # Gather the 'task_title', 'task_desc' and 'due_date' entered by the user.
        task_title = (list(request.POST.values())[list(request.POST.keys()).index('task_title')])
        task_desc = (list(request.POST.values())[list(request.POST.keys()).index('task_desc')])
        due_date = (list(request.POST.values())[list(request.POST.keys()).index('due_date')])
        # Get the current datetime.
        # Don't allow the user to add a past date-time.
        current_date = datetime.now()
        if task_title and task_desc and due_date:
            try:
                due_date = datetime.strptime(due_date, '%m/%d/%Y-%H:%M')
            except ValueError:
                messages.error(request, "Wrong datetime format.")
                return redirect('my_task:index')
            if due_date > current_date:
                new_task = {
                    'creator': request.user,
                    'title': task_title,
                    'description': task_desc,
                    'time_due': due_date,
                }
                # Create a database entry.
                Task.objects.create(**new_task)
                return redirect('my_task:index')
            else:
                messages.error(request, "The due-date should be bigger then now.")
                return redirect('my_task:index')
        elif task_title is '' or task_desc is '' or due_date is '':
            messages.error(request, "Please fill in all form fields.")
            return redirect('my_task:index')

    template_path = 'my_task/tasks.html'
    context = {
        'due_today_and_tomorrow': due_today_and_tomorrow,
        'count_due_today_and_tomorrow': count_due_today_and_tomorrow,
        'over_due': over_due,
        'count_overdue': count_overdue,
        'tasks_all': tasks_all,
        'count_tasks_all': count_tasks_all,
        'tasks_completed': tasks_completed,
        'count_tasks_completed':count_tasks_completed,
    }
    return render(request, template_path, context)

def mark_task_complete(request, task_id):
    """
    """
    try:
        Task.objects.filter(id=task_id).update(status=Task.TASK_COMPLETED)
        messages.success(request, "Task was completed successfully.")
        return redirect("my_task:index")
    except Task.DoesNotExist:
        messages.error(request, "Task was not found in the DB")
        return redirect("my_task:index")

def remove_task(request, task_id):
    """
    """
    try:
        Task.objects.filter(id=task_id).delete()
        messages.success(request, "Task was removed successfully.")
        return redirect("my_task:index")
    except Task.DoesNotExist:
        messages.error(request, "Task was not found in the DB")
        return redirect("my_task:index")








