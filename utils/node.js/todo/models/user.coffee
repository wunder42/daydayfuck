
mongodb = require './db'

# User = (user) ->
# 	this.name = user.name
# 	this.password = user.password
# 	this.email = user.email



class User
	constructor: (@name, @password, @email) ->

	save: ->
		user = {name:this.name, password:this.password, email:this.email}

		mongodb.open (err, db) ->
			console.log err
			# return cb(err) if err
			db.collection 'user', (err, collection) ->
				if err
					mongodb.close()
					return

				collection.insert user {safe: true}, (err, user) ->
					mongodb.close()
					# cb null

	@get: (name, cb) ->
		mongodb.open (err, db) ->
			return cb(err) if err

			db.collection 'user', (err, collection) ->
				if err
					mongodb.close()
					return cb err
				collection.findOne {name:name}, (err, user) ->
					mongodb.close()

					return cb(null, user) if user
					cb err

module.exports = User