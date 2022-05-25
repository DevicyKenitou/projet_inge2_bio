const http = require('http')
const fs = require('fs')
const spawn = require("child_process").spawn;

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

    let dataToReturn;
    if(req.url == '/')
        dataToReturn = GetFile('./interfaceWeb/index.html')
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