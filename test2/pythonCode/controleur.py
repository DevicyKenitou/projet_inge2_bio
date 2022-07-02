import math

from pythonCode.moteur import Moteur, Moteur_Init
from pythonCode.color import printColors

moteur = {
    "1" : None,
    "2" : None
}

LONGUEUR_BRAS = 100 # en centimètre, car dans tout le code, on résonnera en cm
LIMIT_ROTATION = -2

def RadToDeg(val):
    return val * 180 / math.pi

def ModeleInverse(coordXY, longueurBras):

    w1 = coordXY['x']
    w2 = coordXY['y']
    a2 = longueurBras

    q1 = math.atan2(w1, w2)

    val = math.sqrt(w1**2 + w2**2) / a2
    if val > 1 or val < -1:
        print(printColors.WARNING, '>Ces coordonnées ne sont pas atteignable par le robot<', printColors.END)
        return {
            "moteur1" : LIMIT_ROTATION,
            "moteur2" : LIMIT_ROTATION
        }

    q2 = math.acos(val)

    q1 = RadToDeg(q1)
    q2 = RadToDeg(q2)

    return {
        "moteur1" : q1,
        "moteur2" : q2
    }


def SetNewPosition(coordXY):
    # on calcule ici les rotations à associer aux moteurs
    print("Le bras a reçu de nouvelles coordonées :", coordXY)

    # on convertit les coord en rotation de moteurs
    result = ModeleInverse(coordXY, LONGUEUR_BRAS)

    SetRotation(moteur["1"], result["moteur1"])
    SetRotation(moteur["2"], result["moteur2"])


    return {
        'x' : result["moteur1"],
        'y' : result["moteur2"]
    }

# Applique de la rotation à un moteur
# motor => objet Moteur
# rotation en degrées
def SetRotation(motorSelected, rotation):
    # si on est pas dans les limites de rotation, on applique la rotation
    # grâce au modèle inverse, on peut automatiquement déterminer si le bras peut atteindre ou non sa cible
    if rotation != LIMIT_ROTATION:
        motorSelected.Tourner(rotation)
    

def Controleur_Init():
    Moteur_Init()
    moteur["1"] = Moteur('Moteur Base', 26, 19)
    moteur["2"] = Moteur('Moteur Bras', 16, 12)

    return None



if __name__ == "__main__":
    print('Test du modèle inverse et du controleur')
    print("""


    """)
    cible1 = { 'x' : 10, 'y' : 0 }
    print("Coordonées à atteindre:", cible1)
    val1 = ModeleInverse(
        coordXY = cible1,
        longueur = LONGUEUR_BRAS
    )
    print("Moteur 1:", val1[0], "° -Moteur 2:", val1[1], "°\n")

    cible2 = { 'x' : 100, 'y' : 0 }
    print("Coordonées à atteindre:", cible2)
    val2 = ModeleInverse(
        coordXY = cible2,
        longueur = LONGUEUR_BRAS
    )
    print("Moteur 1:", val2[0], "° -Moteur 2:", val2[1], "°\n")


    cible3 = { 'x' : 5, 'y' : 5 }
    print("Coordonées à atteindre:", cible3)
    val3 = ModeleInverse(
        coordXY = cible3,
        longueur = LONGUEUR_BRAS
    )
    print("Moteur 1:", val3[0], "° -Moteur 2:", val3[1], "°\n")



    print("""


    """)
