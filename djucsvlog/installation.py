
INSTALLED_APPS = (
    # other apps
    "djucsvlog",
    )
MIDDLEWARE_CLASSES = (
    'djucsvlog.middleware.LogRequestInfo',
        # other middlewares
    'djucsvlog.middleware.LogViewInfo',
)
UCSVLOG_FILE_VERSION = 'v3'
UCSVLOG_FILE = '/var/log/django/'+\
'my_project/{year}-{month}-{day}-'+\
UCSVLOG_FILE_VERSION+'.ucsv'