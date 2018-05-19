from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    """
    This model holds the database fields of a single task.
    """
    creator = models.ForeignKey(
        User,
        on_delete=models.PROTECT
    )
    title = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )
    description = models.TextField(
        max_length=500,
        null=True,
        blank=True,
    )
    TASK_COMPLETED = 'TASK_COMPLETED'
    TASK_NOT_COMPLETED = 'TASK_NOT_COMPLETED'
    TASK_CHOICES = (
        (TASK_NOT_COMPLETED, "Not completed Task"),
        (TASK_COMPLETED, "Completed Task")
    )
    status = models.CharField(
        max_length=30,
        choices=TASK_CHOICES,
        default=TASK_NOT_COMPLETED,
    )
    time_created = models.DateTimeField(
        'Time Created',
        editable=False,
        auto_now_add=True,
        help_text="Time when a task was first created"
    )
    time_due = models.DateTimeField(
        'Time Due',
        editable=True,
        help_text="Time when a task was set due."
    )

