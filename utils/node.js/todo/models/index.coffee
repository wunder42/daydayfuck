mongoose = require('mongoose');
config = require('../settings');
fs = require('fs');
# log = require('./../libs/log');

mongoose.connect(config.connectionstring);

db = mongoose.connection;
db.on('error', function(err){
    console.error('connect to %s error: ', config.connectionstring, err.message);
    process.exit(1);
});

# db.once 'open', ->
#     log.success('%s has been connected.', config.connectionstring)

models_path = __dirname + '/../models/mapping'
fs.readdirSync(models_path).forEach((file) ->
    require(models_path + '/' + file);
    modelName = file.replace('Model.js', '');
    exports[modelName] = mongoose.model(modelName);
)