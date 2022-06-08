from pythonCode.color import printColors
from pythonCode.controleur import Controleur_Init
from pythonCode.vocalOutput import Vocal_Init
from pythonCode.interfaceWeb import Log


# éxécution que si ce fichier est éxécuté en tant que code principal
if __name__ == "__main__":
    # on appelle sous un try/except pour gérer l'exception de l'arrêt du script par clavier (ctrl+C)
    try:
        Controleur_Init()
        Log('>start')
        Vocal_Init()
    except KeyboardInterrupt:
        None
    finally:
        # message de fin du programme et on informe tous les clients du websockets que la commande vocale a pris fin
        print('Fin du programme 👋')
        Log('>end')