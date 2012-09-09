'Интеграция со стандартным логгером'

LOGGING = {
    'version': 1,
    'filters': {},
    'handlers': {
        'ucsvlog': {
            'class':
            'djucsvlog.logging.handlers'+\
                        '.UCSVLogHandler',
        }
    },
    'loggers': {}
}