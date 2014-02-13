express = require 'express'
path = require 'path'
log4js = require 'log4js'
MongoStore = require('connect-mongo')(express)
settings = require './settings'
routes = require './routes'
app = express()


app.configure ->
	app.set 'views', path.join(__dirname, 'views')
	app.engine 'html', require('ejs').renderFile
	app.use express.bodyParser()
	app.use express.methodOverride()
	app.use express.cookieParser()
	app.use express.session({secret: 'gtd', store: new MongoStore({db:'gtd'})})
	app.use routes(app)
	app.use express.static(path.join(__dirname, 'public'))

app.configure 'development', ->
	app.use(express.errorHandler({ dumpExceptions: true, showStack: true }))

app.configure 'production', ->
	app.use(express.errorHandler())

app.listen 7979