'''
    Меняем формат,
    но остаемся поддерживать старый
    $ python manage.py
        --settings=settings.analytics.v3
'''
from settings.analytics import *
UCSVLOG_FILE_VERSION = 'v3'