import multiprocessing

bind = 'unix:/tmp/gunicorn.sock'
port = 80
workers = (multiprocessing.cpu_count() * 2) + 1

accesslog = '/var/log/access.log'
errorlog = '/var/log/error.log'
