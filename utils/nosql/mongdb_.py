import pymongo, random

connection = pymongo.Connection('127.0.0.1', 27017)

db = connection.knife_d
# print db.collection_names() #show tables
knife_t = db.knife_t

arg = {'name':'intel', 'age':18, 'sex':'man', 'college':'emper'}
args = []

# insert
# knife_t.insert(arg)
# knife_t.save()
# select
print knife_t.find().count(), knife_t.find().sort('age', pymongo.DESCENDING)[0]

for x in knife_t.find():
	arg['name'] = random.randint(1, 100)
	# x.update(arg)
	print x
# # change
# knife_t.save()

# delete