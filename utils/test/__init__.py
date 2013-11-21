from celery_ import add

r = add.delay(4, 4)
r.wait()

