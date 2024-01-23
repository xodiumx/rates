from django.contrib.admin import ModelAdmin, register

from .models import Rates


@register(Rates)
class RatesAdmin(ModelAdmin):
    
    list_display = ('base_currency', 'current_currency', 'price', 'timestamp')
    list_filter = ('base_currency', 'current_currency', 'timestamp')
    search_fields = ('current_currency', )
    empty_value_display = '-пусто-'
