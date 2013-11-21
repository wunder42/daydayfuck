BROKER_URL = 'mongodb://localhost:27017/knife_d'
CELERY_IMPORTS = ('task.add',)

CELERY_RESULT_BACKEND = "mongodb"
CELERY_MONGODB_BACKEND_SETTINGS = {
    "host": "127.0.0.1",
    "port": 27017,
    "database": "knife_d",
    "taskmeta_collection": "knife_t",
}