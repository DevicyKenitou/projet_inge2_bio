
const Q = (e)=> document.querySelector(e);
const ClassSwitch = (elmt, add, remove)=>{
    elmt.classList.add(add);
    elmt.classList.remove(remove);
}

document.addEventListener("DOMContentLoaded", ()=>{

const statut = {}
statut.ws = {}
statut.ws.flag = false
statut.ws.p = Q('#ws_statut'),
statut.ws.indicator = Q('#ws_statut .indicator')

statut.vocal = {}
statut.vocal.p = Q('#vocal_statut'),
statut.vocal.indicator = Q('#vocal_statut .indicator')

const terminal = {}
terminal.elmt = Q('#terminal')
terminal.log = (txt, className='default')=>{
    const line = document.createElement('p')
    line.classList.add('line')
    line.classList.add(className)

    const horodatage = document.createElement('span')
    horodatage.classList.add('horodatage')
    horodatage.innerHTML = new Date().toLocaleTimeString()
    
    const val = document.createElement('span')
    val.classList.add('val')
    val.innerHTML = txt.toString()

    line.appendChild(horodatage)
    line.appendChild(val)
    terminal.elmt.appendChild(line)

    line.scrollIntoView()

}

terminal.info = (txt)=>{
    terminal.log(txt, 'info')
}

terminal.gris = (txt)=>{
    terminal.log(txt, 'gris')
}

terminal.success = (txt) =>{
    terminal.log(txt, 'success')
}

terminal.fail = (txt) =>{
    terminal.log(txt, 'fail')
}

// WEBSOCKET CONNECTION CLIENT

function WSConnect(){
    return new WebSocket('ws://' + hostname + ':8081');
}

const hostname = document.location.hostname ? document.location.hostname : 'localhost'
let socket = WSConnect()
socket.addEventListener('open', function (event) {
    ClassSwitch(statut.ws.p, 'on', 'off');
    statut.ws.flag = true;
});
 
socket.addEventListener('close', ()=>{
    ClassSwitch(statut.ws.p, 'off', 'on');
    statut.ws.flag = false;
    alert("Le Websocket serveur a été déconnecté ou n'est pas disponible, veuillez rafraichir la page pour retenter la connexion.");
});
 
 
socket.addEventListener('message', function (event) {
    console.log(event.data);
    const data = event.data

    if(data == ">start"){
        ClassSwitch(statut.vocal.p, 'on', 'off');
        terminal.info('Commande vocale allumée')
    }
    else if(data == ">end"){
        ClassSwitch(statut.vocal.p, 'off', 'on');
        terminal.info('Commande vocale éteinte')
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
        Q('#moteur1').style.transform = `rotate(${coord.x*2}deg)`
        Q('#moteur2').style.transform = `rotate(${coord.y*2}deg)`

        Q('#moteur1').parentNode.querySelector('.rotation_val').innerHTML = coord.x
        Q('#moteur2').parentNode.querySelector('.rotation_val').innerHTML = coord.y

        terminal.info(json.nom)
        terminal.info(JSON.stringify(coord))
    }
    else if(json.obj == "result"){
        if(json.isPredicted == true)
            terminal.gris('Prédiction : ' + json.result)
        else
            terminal.log('Mot prédit : ' + json.result)
    }
}

window.TreatJSON = TreatJSON

});


/*


TreatJSON({
    obj : 'coord',
    coord : {
        x : 42,
        y : 140
    }
}) 

setTimeout(()=>{
    TreatJSON({
        obj : 'coord',
        coord : {
            x : 100,
            y : 80
        }
    }) 
}, 2000)

*/