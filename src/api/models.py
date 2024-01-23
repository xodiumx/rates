from datetime import datetime

from django.db import models


class Rates(models.Model):
    base_currency = models.CharField(
        'Базовая валютa',
        max_length=10,
        null=False,
        blank=False,
    )
    current_currency = models.CharField(
        'Текущая валюта',
        max_length=10,
        null=False,
        db_index=True
    )
    price = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        null=False,
        blank=False
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
