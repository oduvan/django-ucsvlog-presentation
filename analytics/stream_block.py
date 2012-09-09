from djucsvlog_analytics.analytic_commands\
    import BaseStreamBlockCommand

class Command(BaseStreamBlockCommand):
    '''
        для анализа в потоке не строки
        а сразу блока
    '''
    def collect_block(self,row):
        if row.data_path != '/buy/':
            return
        for data in row.children:
            pass #работаем со всем блоком
                    #данных
