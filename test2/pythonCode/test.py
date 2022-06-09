"""import threading,time
from websocket import WS_Init, WS_SendMessage


def Test(n):
    i=1
    while i<=n:
        print("Main Thread =",i);
        i=i+1
        time.sleep(5)
async def Demo(n):
    await WS_Init('localhost')


if __name__ == "__main__":
    t1 = threading.Thread(target=Test,args=(5,))
    t2=threading.Thread(target=Demo,args=(5,))
    t1.start()
    t2.start()"""


import math

def Euclidienne(coord1, coord2):
    val1 = (coord2['x'] - coord1['x'])**2
    val2 = (coord2['y'] - coord1['y'])**2

    dist = math.sqrt( val1 + val2 )

    return abs(dist)

def RadToDeg(angle):
    return angle * 180 / math.pi

def CoordToRot(targetXY):
    centerXY = { 'x' : 0, 'y' : 0 }
    brasXY = { 'x' : 100, 'y' : 0 }

    A = centerXY
    B = brasXY
    C = targetXY
    Bbis = {
        'x' : 2*A['x'] - B['x'],
        'y' : 2*A['y'] - B['y']
    }

    AC = Euclidienne(A, C)
    AB = Euclidienne(A, B)
    alpha = math.cos( AB/AC )
    alpha = RadToDeg(alpha)

    print(AC, AB, alpha)


CoordToRot({'x' : 0, 'y' : 100})