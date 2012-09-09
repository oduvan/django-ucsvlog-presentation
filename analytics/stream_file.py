from djucsvlog_analytics.analytic_commands\
    import BaseFileStreamCommand

class Command(BaseFileStreamCommand):
    '''
        читаем кучу файлов одновременно
        а строки поступают в
        хронологическом порядке
    '''
    def collect_row(self,row):
        'от самой новой к самой старой'
