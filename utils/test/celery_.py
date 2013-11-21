from celery.task import task

@task
def add(x, y):
	return x + y

# r = add.delay(3, 5)
# r.wait()