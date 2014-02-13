UsersModel = require("./../models").Users
# exports.index = (req, res) ->
# 	res.send {status: true}

# exports.getLoginUser = (req, res) ->
# 	res.send {status: true}	

module.exports = (app) ->
	app.get '/', (req, res) ->
		res.render 'home.html'

	app.post '/u/register', (req, res) ->
		createUser = new UsersModel(req.body)
		return res.json(info: createUser)

	return app.router