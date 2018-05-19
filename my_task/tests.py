from datetime import datetime, timedelta
from django.test import TestCase
from my_task.models import Task
from django.contrib.auth.models import User


class TaskTestCase(TestCase):

    def create_task(self):
        user = User.objects.create(
            username='test_case',
            password='Developer#1234')
        due_date = datetime.now() + timedelta(days=1)
        new_task = {
            'creator': user,
            'title': 'task_title',
            'description': 'task_desc',
            'time_due': due_date,
        }
        return Task.objects.create(**new_task)

    def test_field_label(self):
        task = self.create_task()
        field_label = task._meta.get_field('time_due').verbose_name
        self.assertTrue(field_label, 'Time Due')
