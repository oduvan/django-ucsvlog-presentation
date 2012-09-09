'''
    $ python manage.py  \
     djucsvlog_model_history
'''

#management/commands/
# djucsvlog_model_history.py
from djucsvlog_analytics.analytic_commands\
    import BaseStreamCommand

class Command(BaseStreamCommand):
    pass
