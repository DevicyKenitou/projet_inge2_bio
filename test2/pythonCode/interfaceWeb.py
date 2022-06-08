import json
import urllib
import urllib.parse
import urllib.request
from pythonCode.color import printColors

# permet de print mais aussi d'envoyer des données à notre serveur web (pour l'interface web)
def Log(arg, isJson=False):

    # si nous avons des données au format JSON, il nous faut le convertir en string/texte
    if isJson is True:
        arg = json.dumps(arg, ensure_ascii=False)

    # on affiche dans la console Python les données qui seront envoyés vers le serveur web HTTP
    print(printColors.OKBLUE, arg, printColors.END)

    # on encode les données sous format url, car les données sont passées au par la méthode GET, donc directement injecté dans l'adresse url
    try:
        arg = urllib.parse.quote(arg.encode('utf-8'))
    except AttributeError:
        print('Attribute error')
    except TypeError:
        print('Type error')
    else:
        # si on a pas d'erreur, alors nous envoyons les données vers notre serveur web, qui se chargera de répandre l'information à
        # travers le websocket et les interface web connecté en tant que client du serveur websocket
        try:
            urllib.request.urlopen('http://localhost:8080/vocal/' + arg)
        except:
            print(printColors.FAIL, ">Impossible de se connecter au serveur web (NODE.JS)<", printColors.END)

