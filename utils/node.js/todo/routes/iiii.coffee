
index = require './index'
user = require './user'

module.exports = (app) ->
    app.get '/', index.index
    app.post '/signup', user.signup
    app.post '/login', user.login
    app.get '/logout', user.logout
    app.get '/checklogin', index.getLoginUser
