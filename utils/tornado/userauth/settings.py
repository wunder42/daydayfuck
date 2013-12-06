import pymongo, logging

### database config ###
DB_NAME = 'userauth'
DB_HOST = '127.0.0.1'
DB_PORT = 27017

#########################
mongodb = pymongo.Connection(DB_HOST, DB_PORT)[DB_NAME]
#########################
logging.basicConfig(filename="userauth.log", format="%(asctime)s %(levelname)s %(module)s.%(funcName)s Line:%(lineno)d %(message)s", level=logging.DEBUG)