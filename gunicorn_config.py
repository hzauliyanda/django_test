# -*- coding: utf-8 -*-
"""
------------------------------
 @Date    : 2022/6/29 上午9:46
 @Author  : Cristiano Ronalda
------------------------------
"""
import multiprocessing

# workers = multiprocessing.cpu_count() * 2 + 1
bind = '0.0.0.0:8000'
reload = True
pidfile = '/Users/liyanda/Documents/project_code/python/django_test/gunicirn_file/gunicorn.pid'
# accesslog = '/usr/src/app/logs/gunicorn_acess.log'
accesslog = '/Users/liyanda/Documents/project_code/python/django_test/logs/mytest.log'
# errorlog = '/usr/src/app/logs/gunicorn_error.log'
errorlog = '/Users/liyanda/Documents/project_code/python/django_test/logs/mytest.log'
# CMD ["/usr/local/bin/gunicorn", "-c", "/usr/src/app/configs/gunicorn_config.py", "django_test.wsgi"]
# gunicorn -c ./gunicorn_config.py django_test.wsgi
# /Users/liyanda/Documents/project_code/python/django_test/gunicorn_config.py