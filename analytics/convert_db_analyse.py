from djucsvlog_analytics.analytic_commands\
    import (BaseAnalyticReadCommand,
            BaseAnalyticElement)

class TopUsersElement(BaseAnalyticElement):
    '''кусочек анализа'''

class Command(BaseAnalyticReadCommand):
    '''используем кусочки
        и собираем их в полноценный
            отчет'''
    def initial_options(self, options):
        super(Command, self).initial_options(options)
        self.add_analyse_element(
            TopUsersElement())