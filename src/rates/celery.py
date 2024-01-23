from __future__ import absolute_import

import os

from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rates.settings')

app = Celery('rates')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'get-rate-of-usd': {
        'task': 'api.tasks.get_current_usd_rate',
        'schedule': crontab(minute='*/1'),
    },
}
app.autodiscover_tasks()

app.conf.timezone = 'UTC'
