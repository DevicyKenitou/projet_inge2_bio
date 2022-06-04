moteur = {
    "1" : None,
    "2" : None
}

def SetNewPosition(coordXY):
    # on calcule ici les rotations à associer aux moteurs
    print("Le bras a reçu de nouvelles coordonées :", coordXY)

    # TODO on devra convertir les coord en rotation de moteurs

    SetRotation(moteur["1"], coordXY["x"])
    SetRotation(moteur["2"], coordXY["y"])


    return None

# Applique de la rotation à un moteur
# motor => objet Moteur
# rotation en degrées
def SetRotation(motorSelected, rotation):
    # TODO vérifier si on est pas dans les limites de rotation

    motorSelected.Tourner(rotation)
    return None

def Controleur_Init():

    moteur["1"] = Moteur('Moteur Base')
    moteur["2"] = Moteur('Moteur Bras')

    return None

class Moteur:
    def __init__(self, name='moteur sans nom'):
        self.currentRotation = 0 # la rotation acutelle en degrée
        self.pas = 1
        self.rotation = 2
        self.coefPasRotation = self.pas / self.rotation # 1 pas = 2° de rotation
        self.name = name

    def Tourner(self, rotation):
        # ici on met le code de Juliette pour tourner tel ou tel moteur

        print("Le moteur", self.name, "a tourné de", rotation)

        return None