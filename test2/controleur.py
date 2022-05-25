def SetNewPosition(coordXY):
    # on calcule ici les rotations à associer aux moteurs
    print("Le bras a reçu de nouvelles coordonées :", coordXY)
    return None

# Applique de la rotation à un moteur
# motor => objet Moteur
# rotation en degrées
def SetRotation(motor, rotation):
    return None


class Moteur:
    def __init__(self):
        self.currentRotation = 0 # la rotation acutelle en degrée
        self.pas = 1
        self.rotation = 2
        self.coefPasRotation = self.pas / self.rotation # 1 pas = 2° de rotation

    def Tourner(self):
        # ici on met le code de Juliette pour tourner tel ou tel moteur
        return None