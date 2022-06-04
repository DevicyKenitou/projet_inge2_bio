#!/usr/bin/env python

"""
https://websockets.readthedocs.io/en/stable/intro/quickstart.html#broadcast-messages
"""
import asyncio
import datetime
import random
import websockets

CONNECTIONS = set()
_message = "test websocket message"
_previousMessage = ""

async def register(websocket):
    CONNECTIONS.add(websocket)
    print("+ Nouveau client WS")
    try:
        await websocket.wait_closed()
    finally:
        CONNECTIONS.remove(websocket)
        print("- Client WS parti")

async def spread_infos():

    global _message, _previousMessage

    while True:
        if _message != _previousMessage:
            #message = datetime.datetime.utcnow().isoformat() + "Z"
            websockets.broadcast(CONNECTIONS, _message)
            _previousMessage = _message
            print('>>>', _message)
        
        await asyncio.sleep(0.5) # en seconde


async def WS_Init(wsIpAdress):
    print(wsIpAdress)
    async with websockets.serve(register, wsIpAdress, 8001):
        print("Websocket starting at ip :", wsIpAdress)
        await spread_infos()


# Les fonctions à importer dans d'autres fichiers
def WS_SendMessage(msg):
    message = msg
    triggered = True

def StartWS(wsIpAdress='localhost'):
    #asyncio.run(main(wsIpAdress))
    print("OKOK")


if __name__ == "__main__":
    StartWS("192.168.1.34")

