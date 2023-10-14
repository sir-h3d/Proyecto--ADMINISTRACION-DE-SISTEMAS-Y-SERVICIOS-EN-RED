const mongoose = require('mongoose')

mongoose.connect('mongodb://127.0.0.1:27017/connection_ssh', {
    useNewUrlParser: true,
},
(err) => {
    if (!err) {
        console.log('Connection suceeded');
    } else {
        console.log('Error in connection' + err);
    }
});

require('./routes.model');


