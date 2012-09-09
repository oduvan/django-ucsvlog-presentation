'''
    djucsvlog.components.change_model
    Ищу виновных
'''

UCSVLOG_CHANGE_MODEL = [
    {'model':'statistics.Banner',
    'props':['pk','name',
    'campaign.pk','picture.url']},

    {'model':'statistics.UserProfile',
    'props':['user.pk','user.username',
             'balance']}
]