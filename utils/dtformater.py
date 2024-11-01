from datetime import datetime

from pytz import timezone


def shorten_datetime(datetime_string: str) -> str:
    dt = datetime.strptime(datetime_string, '%Y-%m-%dT%H:%M:%S.%fZ')
    utc_timezone = timezone('UTC')
    ukraine_timezone = timezone('Europe/Kiev')
    dt_utc_aware = utc_timezone.localize(dt)
    dt_ukraine = dt_utc_aware.astimezone(ukraine_timezone)
    custom_format = dt_ukraine.strftime('%H:%M %d.%m')
    return custom_format
