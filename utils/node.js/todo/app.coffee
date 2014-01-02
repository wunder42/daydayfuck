express = require 'express'
path = require 'path'
log4js = require 'log4js'

log4js.configure {
	appenders: [
		{type: 'console'},
		{
			type: 'file',
			filename: 'access.log',
			maxLogSize: 1024 * 1024,
			category: 'normal'
		}
	]
}

logger = log4js.getLogger 'normal'
logger.setLevel 'INFO'

app = express()
app.use express.bodyParser()
server = (require 'http').createServer app
# io = (require 'socket.io').listen server

app.use log4js.connectLogger logger, {level:log4js.levels.INFO}

# fs = require('fs');
# accessLogfile = fs.createWriteStream('access.log', {flags: 'a'});
# errorLogfile = fs.createWriteStream('error.log', {flags: 'a'});

# app.use(express.logger({stream: accessLogfile}));

# app.configure 'production', ->
#   app.use (err, req, res, next) ->
#     meta = '[' + new Date() + '] ' + req.url + '\n';
#     errorLogfile.write(meta + err.stack + '\n');
#     next();

app.set 'views', path.join(__dirname, 'views')
# app.engine '.html', ejs.__express
app.engine 'html', require('ejs').renderFile
# app.set 'view engine', 'ejs'

app.use express.static(path.join(__dirname, 'public'))
app.use require('connect-assets')()

app.get '/', (req, res) ->
	res.render 'home.html'
	# res.render path.normalize(__dirname + '/../views/index.html')

app.get '/m/add', (req, res) ->
	logger.info req.query.content
	res.send {success: 'success'}

app.get '/u/register', (req, res) ->

app.post '/u/login', (req, res) ->
	# logger.info req.query.username, req.query.password
	# logger.info req.body.men
	res.send {success: req.body.men}

app.get '/u/logout', (req, res) ->

# @todos = {}
# io.sockets.on 'connection', (socket) =>
# 	console.log 'connected...'
# 	socket.on 'joinList', (list) => 
# 		console.log "join list #{list}"
# 		socket.list = list
# 		socket.join list
# 		@todos[list] ?= []
# 		socket.emit 'syncItems', @todos[list]

# 		socket.on 'newItem', (todo) =>
# 			console.log "new todo #{todo.title}"
# 			@todos[list].push todo
# 			io.sockets.in(socket.list).emit('itemAdded', todo)

# 		socket.on 'removeItem', (id) =>
# 			@todos[list] = @todos[list].filter (item) -> item.id isnt id
# 			io.sockets.in(socket.list).emit('itemRemoved', id)

# handleNewItem = (socket) ->
server.listen 7878


