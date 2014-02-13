UsersModel = require("./../models").Users
path = require('path')

exports.signup = (req, res) ->
	createUser = new UsersModel(req.body);
    UsersModel.findOne({name:req.body.name}, (err, user) ->
        if (err)
            return res.json({err:err});
        if (user) {
            return res.json({err:"hava one"});
        }
        createUser.save((err, user) ->
            if (err) {
                return res.json({err:err});
            }
            req.session["user"] = user;
            res.json();
        );
    );

exports.login = (req, res) ->
	res.send {status: true}

exports.logout = (req, res) ->
	res.send {status: true}

