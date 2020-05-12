from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'traxee.settings')

# celery = Celery('task', broker='redis://127.0.0.1:6379')
# celery.config_from_object(celery)

app = Celery('traxee', broker='redis://127.0.0.1:6379')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))