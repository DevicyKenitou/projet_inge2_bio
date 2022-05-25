
const Q = (e)=> document.querySelector(e);
document.addEventListener("DOMContentLoaded", ()=>{

const statut = {}
statut.p = Q('#ws_statut'),
statut.text = Q('#ws_statut span')

// WEBSOCKET CONNECTION CLIENT
const hostname = document.location.hostname ? document.location.hostname : 'localhost'
const socket = new WebSocket('ws://' + hostname + ':8001');
socket.addEventListener('open', function (event) {
    statut.text.innerHTML = 'ON';
});
 
socket.addEventListener('close', ()=>{
    statut.text.innerHTML = 'OFF';
});
 
 
socket.addEventListener('message', function (event) {
    console.log(event.data);
});
 
const contactServer = (str) => {
    socket.send(str);
};


});