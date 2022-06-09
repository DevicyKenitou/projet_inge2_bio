import threading,time
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
    t2.start()