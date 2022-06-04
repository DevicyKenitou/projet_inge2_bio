
const Q = (e)=> document.querySelector(e);
document.addEventListener("DOMContentLoaded", ()=>{

const statut = {}
statut.ws = {}
statut.ws.p = Q('#ws_statut'),
statut.ws.text = Q('#ws_statut span')

statut.vocal = {}
statut.vocal.p = Q('#vocal_statut'),
statut.vocal.text = Q('#vocal_statut span')

// WEBSOCKET CONNECTION CLIENT
const hostname = document.location.hostname ? document.location.hostname : 'localhost'
const socket = new WebSocket('ws://' + hostname + ':8081');
socket.addEventListener('open', function (event) {
    statut.ws.text.innerHTML = 'ON';
});
 
socket.addEventListener('close', ()=>{
    statut.ws.text.innerHTML = 'OFF';
});
 
 
socket.addEventListener('message', function (event) {
    console.log(event.data);
    const data = event.data

    if(data == ">start"){
        statut.vocal.text.innerHTML = 'ON';
    }
    else if(data == ">end"){
        statut.vocal.text.innerHTML = 'OFF';
    }
    else
        try{
            TreatJSON(JSON.parse(data))
        }catch(e){
            console.error(e);
        }
});
 
const contactServer = (str) => {
    socket.send(str);
};

function TreatJSON(json){

    if(json.obj == 'coord'){
        const coord = json.coord;
        Q('#moteur1 img').style.transform = `rotate(${coord.x*2}deg)`

    }
}


});