import json
import time

from pythonCode.vocal import Vocal_Launch, Vocal_IsListening, Vocal_GetListeningStatus
from pythonCode.controleur import SetNewPosition
from pythonCode.dico import dicoNb
from pythonCode.color import printColors
from pythonCode.interfaceWeb import Log
from CONST import __Is_Running_On_Raspberry__


# pour les tests sans Raspberry, on ne peut pas utiliser les ports GPiO,
# donc on désactive les fonctions de contrôle des moteurs

if __Is_Running_On_Raspberry__ is True:
    from pythonCode.pince import Pince_Test
    print(printColors.HEADER, ">Code lancer sur une Raspberry<", printColors.END)
else:
    def Pince_Test(): 
        print('Ouverture de la pince puis fermecture')
    print(printColors.HEADER, ">Code lancer sans port GPio (non RAspberry)<", printColors.END)



# l'initialisation du vocal et tout simplement le lancement de l'algo Vosk, en passant en paramètre la fonction
# _OnPredict_ pour récupérer et traiter le résultat fourni par Vosk
def Vocal_Init():
    Vocal_Launch(_OnPredict_)


# Quand un résultat est fourni par Vosk (qu'il soit prédit ou final), on va traiter les données
# dans le but de déterminer les actions à effectuer par notre bras
def _OnPredict_(result, isPredicted):

    # on convertit les données reçu en JSON/dictionnaire Python, pour pouvoir extraire uniquement le mot en string
    result = json.loads(result)

    # en fonction de si la valeur est prédite ou final, Vosk nous renvoie dans des clés de nom différent dans le JSON
    if isPredicted is True:
        result = result['partial']
    else:
        result = result['text']

    # on convertit le mot/texte en miniscule, pour macther correctement avec les mots de notre propre dictionnaire/vocabulaire de mot à connaitre
    result = result.lower()

    # si le résultat n'est pas une chaine de caractères vide, on va donc l'analyser/l'interpréter
    if result != "":
        # on coupe la réception de données du micro, en attendant que l'algo Vosk nous renvoie le mot qu'il a reconnu
        Vocal_IsListening(False)

        # on affiche les résultats, et on l'envoie en même temps aux interfaces web
        Log({
            "obj" : 'result',
            "result" : result,
            "isPredicted" : isPredicted
        }, isJson=True)

        # si c'est une valeur finale, on va l'interpréter
        if isPredicted is False:
            OnResult(result)
            Vocal_IsListening(True)
        # sinon si c'est une valeur prédite, on attend la valeur finale (et on ne réactive pas le micro)
    else :
        # si le résultat est vide, on active alors le micro pour analyser l'audio et obtenir un résultat
        if Vocal_GetListeningStatus() is False:
            Vocal_IsListening(True)


def OnResult(result):
    if result in dicoNb:
        print(dicoNb[result])
        coord = dicoNb[result]['coordXY']
        SetNewPosition(coord)
        Log({
            "nom" : dicoNb[result]["nom"],
            "obj" : 'coord',
            "coord" : coord
        }, isJson=True)

        # on attend 2 secondes avant la prochaine commande
        time.sleep(2)
    else:
        if result == "attraper":
            Pince_Test()
            # on attend 1 secondes avant la prochaine commande
            time.sleep(1)
        else :
            print(printColors.WARNING, '>Commande vocale inconnue<', printColors.END)