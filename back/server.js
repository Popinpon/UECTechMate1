const ws = require('ws').Server;
const fs = require('fs');
const wsServer = new ws({ port: 5001 });

wsServer.on('connection', server => {
    server.on('message', message => {
        const obj = JSON.parse(message)
        if (obj.room_type == "A") {
            var json_data = fs.readFileSync("../dist/static/responses/roomA.json")
            const list = JSON.parse(json_data);
            list.push(obj);
            if (list.length >= 10)
                list.shift();
            fs.writeFile("../dist/static/responses/roomA.json", JSON.stringify(list), (err) => {
                if (err) throw err;
                console.log('ファイルが正常に出力されました。');
            })
        } else if (obj.room_type == "B") {
            var json_data = fs.readFileSync("../dist/static/responses/roomB.json")
            const list = JSON.parse(json_data);
            list.push(obj);
            if (list.length >= 10)
                list.shift();
            fs.writeFile("../dist/static/responses/roomB.json", JSON.stringify(list), (err) => {
                if (err) throw err;
                console.log('ファイルが正常に出力されました。');
            })
        } else {
            var json_data = fs.readFileSync("../dist/static/responses/roomC.json")
            const list = JSON.parse(json_data);
            list.push(obj);
            if (list.length >= 10)
                list.shift();
            fs.writeFile("../dist/static/responses/roomC.json", JSON.stringify(list), (err) => {
                if (err) throw err;
                console.log('ファイルが正常に出力されました。');
            })
        }


        wsServer.clients.forEach(client => {
            client.send(message);
        });
    });
});

console.log('websocket起動中...');