from time import sleep
from CONST import __Is_Running_On_Raspberry__

if __Is_Running_On_Raspberry__ is True:
    import RPi.GPIO as GPIO
else:
    def GPIO(): return None

DIR = 20    # sens de rotation au port GPIO20
STEP = 21   # GPIO 

# sens => 
CW =1 # horloge
CCW = 0 # anti

# un tour (step)
SPR = 48
step_total = SPR #1 rotation
delay = .0208

def Moteur_Init():
    if __Is_Running_On_Raspberry__ is True:
        GPIO.setmode(GPIO.BCM)


class Moteur:
    def __init__(self, name, _dir, _step):
        self.currentRotation = 0 # la rotation acutelle en degrée
        self.pas = 1
        self.rotation = 1.8
        self.coefPasRotation = self.pas / self.rotation # 1 pas = 2° de rotation
        self.name = name

        self._dir = _dir
        self._step = _step

        if __Is_Running_On_Raspberry__ is True:
            GPIO.setup(_dir, GPIO.OUT)
            GPIO.setup(_step, GPIO.OUT)

    def Tourner(self, rotation):
        step = int(self.coefPasRotation * rotation)

        print("Le moteur", self.name, "a tourné de", rotation, '° =', step, 'steps')
        self.currentRotation = rotation
        self.ApplyStep(step)

    def ApplyStep(self, step):

        if __Is_Running_On_Raspberry__ is False:
            return None
        # sens
        if step < 0:
            GPIO.output(self._dir, CCW)
        else:
            GPIO.output(self._dir, CW)

        step_count = abs(step)

        for x in range (step_count):
            GPIO.output(self._step, GPIO.HIGH)
            sleep(delay)
            GPIO.output(self._step, GPIO.LOW)
            sleep(delay)


if __name__ == "__main__":
    print("test")

    Moteur_Init()

    m = Moteur("Moteur test", 20, 21)
    m.ApplyStep(24)
    sleep(2)
    m.ApplyStep(-24)