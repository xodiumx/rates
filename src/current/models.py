from datetime import datetime

from django.db import models


class Rates(models.Model):
    base_rate = models.CharField(
        'Базовая валюту',
        max_length=10,
        null=False,
        blank=False,
    )
    current_rate = models.CharField(
        'Курс валюты',
        max_length=10,
        null=False,
        default=datetime.now,
        db_index=True
    )
    timestamp = models.DateTimeField(
        'Текущее время',
        null=False,
        default=datetime.now,
    )

    class Meta:
        verbose_name = 'Курс валюты'
        verbose_name_plural = 'Курсы валют'
        ordering = ('timestamp',)
