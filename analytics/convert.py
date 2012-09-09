from djucsvlog_analytics.convert_commands\
            import BaseConvertBlockCommand

class Command(BaseConvertBlockCommand):
    ''' конвертируем логи '''
    def convert_row(self,row):
        'конвертируем данные'
    def convert_call_data(self,row):
        'конвертируем данные вызова'
        return []

UCSVLOG_CONVERT_REQUEST_FIELDS
UCSVLOG_CONVERT_RESPONSE_FIELDS
UCSVLOG_CONVERT_VIEW_OPEN_FIELDS