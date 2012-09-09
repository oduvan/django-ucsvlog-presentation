# time call_info data
SYSLOG = '''
2012-09-08T08:45:23 oduvan GET /
2012-09-08T08:45:24 oduvan response
status 200
2012-09-08T08:47:23 oduvan GET /news/
2012-09-08T08:47:24 oduvan response
status 200
2012-09-08T08:48:24 oduvan GET /reg/
2012-09-08T08:48:27 oduvan unhandled
exception
AttributeError: 'datetime.datetime'
object has no attribute 'reg'
'''