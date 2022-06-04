import json
import urllib
import urllib.parse

import urllib.request

from vocal import Vocal_Init
from controleur import Controleur_Init, SetNewPosition
from dico import dicoNb

def _OnPredict_(result, isPredicted):
    result = json.loads(result)

    if isPredicted is True:
        result = result['partial']
    else:
        result = result['text']

    result = result.lower()

    if result != "":
        print(result, isPredicted)

        Log({
            "obj" : 'result',
            "result" : result,
            "isPredicted" : isPredicted
        }, isJson=True)

        if isPredicted is False:
            if result in dicoNb:
                print(dicoNb[result])
                coord = dicoNb[result]['coordXY']
                SetNewPosition(coord)
                Log({
                    "obj" : 'coord',
                    "coord" : coord
                }, isJson=True)
            else:
                print('>Emplacement inconnue<')


def Log(arg, isJson=False):
    if isJson is True:
        arg = json.dumps(arg, ensure_ascii=False)

    print(arg)

    arg = urllib.parse.quote(arg.encode('utf-8'))

    try:
        arg = urllib.parse.quote(arg.encode('utf-8'))
    except AttributeError:
        print('Attribute error')
    except TypeError:
        print('Type error')
    else:
        urllib.request.urlopen('http://localhost:8080/vocal/' + arg)


if __name__ == "__main__":

    Controleur_Init()

    try:
        Log('>start')
        Vocal_Init(_OnPredict_)
    except KeyboardInterrupt:
        None
    finally:
        print('Bye 👋')
        Log('>end')