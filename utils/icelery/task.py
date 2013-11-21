
from celery import Celery

celery = Celery('tasks', backend= \
	'redis://localhost:6379/1', broker='redis://localhost:6379/1')

@celery.task
def add(x, y):
    return x + y
