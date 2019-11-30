import gevent.monkey

gevent.monkey.patch_all()

import multiprocessing

# debug = True
loglevel = 'info'
bind = "0.0.0.0:8000"
pidfile = "app/logs/gunicorn.pid"
accesslog = "app/logs/gaccess.log"
errorlog = "app/logs/gdebug.log"
daemon = True

# 启动的进程数
workers = multiprocessing.cpu_count()
worker_class = 'gevent'
x_forwarded_for_header = 'X-FORWARDED-FOR'
