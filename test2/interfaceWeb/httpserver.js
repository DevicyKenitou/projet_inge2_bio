const http = require('http')
const fs = require('fs')
const spawn = require("child_process").spawn;

const WebSocket = require('ws');
const {WebSocketServer} = require('ws');

// https://quizdeveloper.com/faq/how-can-i-get-local-ip-address-in-nodedotjs-server-aid1245
const clientIp = Object.values(require("os").networkInterfaces())
                        .flat()
                        .filter((item) => !item.internal && item.family === "IPv4")
                        .find(Boolean).address;

const GetFile = (path) => {
    try{
        return fs.readFileSync(path)
    }catch(err){
        return err.toString()
    }
};

const PORT = 8080
const server = http.createServer((req, res)=>{

    console.log("Requête reçu : ", req.url)

    let dataToReturn;
    if(req.url == '/')
        dataToReturn = GetFile('./interfaceWeb/index.html')
    else if(req.url.startsWith('/vocal/')){
        dataToReturn = 'ok'
        FromPython(req.url)
    }
    else
        dataToReturn = GetFile('./interfaceWeb' + req.url )
    res.end(dataToReturn)
})

server.listen(8080, '', '', console.log('Server Web Ready at http://' + clientIp + ':' + PORT))

/*
const process = spawn("python3", ['-u', './main.py', clientIp]);
process.stdout.on('data', (data)=>{
    const txt = data.toString().replace(/([\n])$/, '')
    console.log("\x1b[35m" + txt + "\x1b[0m")
})*/

function FromPython(url){
    let data = url.replace(/^\/vocal\//, '')
    data = decodeURIComponent(data)

    console.log("Données reçu depuis Python (vocal):", data)

    SendTOAllClient(data)
}


// WS Init


const wss = new WebSocketServer({ port: 8081 });
let wsData = {
    vocalStatusOn : false
}
wss.on('connection', function connection(ws) {

    console.log("New client connected")
    ws.on('message', function message(data, isBinary) {
        //WSServer.ReceiveFromClient(ws, data.toString());
        console.log("WS => ", data.toString())
    });
});

function SendTOAllClient(value, selfClient=null){
    wss.clients.forEach((client)=>{

        // if the client that trigger this call is specified, we don't send the response to him
        if(selfClient != null && selfClient == client)
            return;

        if (client.readyState === WebSocket.OPEN) {
            client.send(value.toString());
        }

    })
}