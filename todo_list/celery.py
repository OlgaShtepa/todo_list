from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_list.settings')

app = Celery('todo_list')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(['base'])
