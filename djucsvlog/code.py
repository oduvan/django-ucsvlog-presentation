
#используем глобальный объект
from djucsvlog import glog

glog('Something happens') #строка
glog.err('Something important') #важно
# открываем дерево
glog.a_log('USER_INFO', ['ID', 5678])
# вносим массивы данных
glog(['Name', 'Alexander'])
glog(['Info','Lyabah','a@lyabah.com'])
# закрываем дерево
glog.c_log('USER_INFO')