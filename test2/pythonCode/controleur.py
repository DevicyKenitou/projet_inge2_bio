from pythonCode.moteur import Moteur, Moteur_Init

moteur = {
    "1" : None,
    "2" : None
}

def SetNewPosition(coordXY):
    # on calcule ici les rotations à associer aux moteurs
    print("Le bras a reçu de nouvelles coordonées :", coordXY)

    # TODO on devra convertir les coord en rotation de moteurs

    SetRotation(moteur["1"], coordXY["x"])
    #SetRotation(moteur["2"], coordXY["y"])


    return None

# Applique de la rotation à un moteur
# motor => objet Moteur
# rotation en degrées
def SetRotation(motorSelected, rotation):
    # TODO vérifier si on est pas dans les limites de rotation

    motorSelected.Tourner(rotation)
    return None

def Controleur_Init():
    Moteur_Init()
    moteur["1"] = Moteur('Moteur Base', 20, 21)
    #moteur["2"] = Moteur('Moteur Bras', 20, 21)

    return None