const ws = require('ws').Server;
const wsServer = new ws({ port: 5001 });

wsServer.on('connection', server => {
    server.on('message', message => {
        console.log(message);
        wsServer.clients.forEach(client => {
            client.send(message);
        });
    });
});

console.log('websocket起動中...');