from celery import Celery 
# from celery.task import task
celery = Celery('hello', broker='redis://localhost:6379/1', backend = 'redis://localhost:6379/1')

celery.conf.update(
    CELERY_TASK_RESULT_EXPIRES=10,
)

@celery.task
def add(x, y):
	return x + y

@celery.task
def hello():
	return 'hello, world'

# r = hello.delay()
# r.get(timeout=1)
# result = add.delay(8, 9)
# result.wait()
# hello.apply_async(queue='lopri', countdown=10)

