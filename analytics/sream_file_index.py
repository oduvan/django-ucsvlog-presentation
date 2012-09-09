from djucsvlog_analytics.analytic_commands\
    import BaseStreamCommand
class Command(BaseStreamCommand):
    '''Читаем в потоке, только есть еще
        индексный файл для переодической
        дочитки'''
UCSVLOG_STREAM_INDEX = 'index_file.db'
UCSVLOG_STREAM_FOLDERS_MATCHES_RE = {
    '/var/log/django/':[
re.compile('front\-'+UCSVLOG_FILE_VERSION+\
           '\.ucsv'),],
    '/var/log/django4/':[
re.compile('front\-'+UCSVLOG_FILE_VERSION+\
           '\.ucsv'),]}
