
mongoose = require('mongoose'),
    Schema = mongoose.Schema,
    crypto = require('crypto');

schema = new Schema({
    name:String,
    hash_password:String
});

schema.virtual("password").set (password) ->
    this.hash_password = encryptPassword(password)

schema.method "authenticate", (plainText) ->
    return encryptPassword(plainText) === this.hash_password


encryptPassword = (password) ->
    return crypto.createHash("md5").update(password).digest("base64")

mongoose.model('Users', schema);