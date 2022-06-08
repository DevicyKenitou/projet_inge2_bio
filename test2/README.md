# Les prérequis 

## Les outils de développement
- Python3.X
- Pip3

## Les dépendances/librairie

1. Pour Python (Commande vocale + Controle des moteurs)

Faire `pip3 install requirements.txt`
Les versions utilisées dans ce projet sont : 
```
sounddevice==0.4.4
vosk==0.3.42
```

2. Pour Node.js (Pour l'interface utilisateur / web)

Faire `npm install`
Il n'y a qu'une dépendance à installer, qui est celui du Websocket serveur
`ws=8.7.0`

# Lancer les programmes

Il faudra 2 consoles/terminals de lancement :
- Pour Python : `python3 main.py`
- Pour Node.js : `node interfaceWeb/httpserver.js`

_________

Pour éxcuter le code sur un ordinateur (non Raspberry), il faut changer la variable `__Is_Running_On_Raspberry__` tel que :
`__Is_Running_On_Raspberry__ = False`
Pour une éxécution sur Raspberry (si les moteurs sont branchés sur les PORT GPio):
`__Is_Running_On_Raspberry__ = True`

Normalement un message en violet s'affiche au lancement du programme Python indiquant si cette variable est True ou False

__________

Pour ouvrir l'interface utilisateur, juste ctrl+clique sur le lien qui s'affiche dans la console où est lancée `node interfaceWeb/httpserver.js`
L'adresse URL en local est : `http://localhost:8080/`