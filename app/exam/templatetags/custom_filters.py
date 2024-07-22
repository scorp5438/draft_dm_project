from django import template
from datetime import timedelta, datetime

register = template.Library()


@register.filter
def add_minutes(value, minutes):
    # Преобразуем значение времени в datetime
    datetime_value = datetime.combine(datetime.today(), value)
    # Добавляем минуты
    new_time = (datetime_value + timedelta(minutes=minutes)).time()
    return new_time.strftime('%H:%M')
