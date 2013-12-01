import pymongo, sys

sys.path.append('/home/knife/dev/codehub/daydayfuck/zainar/1/xiaobao/')
import settings

con = pymongo.Connection(host = settings.MONGO_HOST, port = int(settings.MONGO_PORT))
db = con[settings.DB_NAME]

# db.t_user.remove()

for x in db.text_joke.find():
	print x