'''
    $ python manage.py  \
    djucsvlog_user_path_convertor   \
    --out=2012-08.user_path.db  \
    /var/logs/2012-08-*
'''

TABLES = {
    'host':{
        'useruuid':{
            'request':{
                'request_log':[]
            }}}}