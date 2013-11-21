from task import hello, add
import celery
# import celery
# print add.delay(1, 2)

query = celery.events.state.tasks_by_type('hello')
print query