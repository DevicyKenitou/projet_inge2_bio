import json
import asyncio
import sys

from vocal import Vocal_Init
from websocket import WS_Init, WS_SendMessage
from controleur import SetNewPosition

dicoNb = {
    "un" : {
        "nom" : "emplacement 1",
        "coordXY" : {'x' : 10, 'y' : 20}
    },
    "deux" : {
        "nom" : "emplacement 2",
        "coordXY" : {'x' : 20, 'y' : 20}
    },
    "trois" : {
        "nom" : "emplacement 3",
        "coordXY" : {'x' : 30, 'y' : 20}
    },
    "quatre" : {
        "nom" : "emplacement 4",
        "coordXY" : {'x' : 40, 'y' : 20}
    },
    "cinq" :{
        "nom" : "emplacement 5",
        "coordXY" : {'x' : 50, 'y' : 20}
    }
}

def _OnPredict_(result, isPredicted):
    result = json.loads(result)

    if isPredicted is True:
        result = result['partial']
    else:
        result = result['text']

    result = result.lower()

    if result != "":
        print(result, isPredicted)
        #WS_SendMessage(json.dumps({result : result}))

        if isPredicted is False:

            if result in dicoNb:
                print(dicoNb[result])
                SetNewPosition(dicoNb[result]['coordXY'])
            else:
                print('>Emplacement inconnue<')

            




def thread_StartVocal():
    print('+ Thread Vocal')

def thread_WS():
    print('+ Thread WS')


async def main(wsIpAdress):
    input_coroutines = [WS_Init(wsIpAdress), Vocal_Init(_OnPredict_)]
    await asyncio.gather(*input_coroutines, return_exceptions=True)



argv = sys.argv
wsIpAdress = "localhost"
if __name__ == "__main__":
    if len(argv) > 1:
        wsIpAdress = argv[1]
    asyncio.run(main(wsIpAdress))