from djucsvlog_analytics.analytic_commands\
        import BaseSimpleAnalyticCommand

class Command(BaseSimpleAnalyticCommand):
    '''
        самый базовый анализатор.
        Читаем файл за файлом,
        строку за строкой
    '''
    def collect_row(self,row):
        '''
            анализируем строку
        '''