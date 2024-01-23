import requests

from rates.celery import app
from rates.settings import API_KEY

from .models import Rates

time_to_request = 60
current_currency = 'RUB'


@app.task(time_limit=120)
def get_current_usd_rate() -> str:
    """
    - Функция получения текущего курса доллара к рублю.
    - Работает каждые 60 секунд и создает в базе записи
      о текущем курсе доллара к рублю
    - endp - эндпоинт для получения информации о курсе параметры:
      base - Базовая валюта
      symbols - список кодов валют через запятую, для получения информации о них
    """
    endp = f'https://api.apilayer.com/exchangerates_data/latest?base=USD&symbols={current_currency}'
    headers = {'apikey': API_KEY}
    try:
        response = requests.get(endp, headers=headers).json()
        price = response.get('rates').get('RUB')
    except Exception as err:
        return f'Ошибка в запросе {err}'

    data = {
        'base_currency': 'USD',
        'current_currency': current_currency,
        'price': price
    }
    Rates.objects.create(**data)
    return 'Данные успешно занесены в базу'
