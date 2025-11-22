# cercle.py

from math import pi

class Cercle:
    def __init__(self, rayon: float):
        self.rayon = rayon                      # le setter est appelé ici

    # Propriété en écriture contrôlée
    @property
    def rayon(self) -> float:
        return self._rayon

    @rayon.setter
    def rayon(self, valeur: float):
        if valeur <= 0:
            raise ValueError("Le rayon doit être strictement positif !")
        self._rayon = valeur

    # Propriétés calculées
    @property
    def perimetre(self) -> float:
        return 2 * pi * self._rayon

    @property
    def surface(self) -> float:
        return pi * self._rayon ** 2

    # Méthode bonus : agrandir le cercle
    def agrandir(self, pourcentage: float):
        if pourcentage < 0:
            raise ValueError("Le pourcentage doit être positif")
        self.rayon *= (1 + pourcentage / 100)


# =============== TEST / DÉMO ===============
if __name__ == "__main__":
    c = Cercle(3)

    print(f"Périmètre : {c.perimetre:.2f}")   # → 18.85
    print(f"Surface   : {c.surface:.2f}")     # → 28.27

    # Test de l'agrandissement (+50%)
    c.agrandir(50)
    print(f"\nAprès +50% :")
    print(f"Nouveau rayon    : {c.rayon:.2f}")
    print(f"Nouveau périmètre: {c.perimetre:.2f}")
    print(f"Nouvelle surface : {c.surface:.2f}")

    # Test d'erreur
    try:
        Cercle(-5)
    except ValueError as e:
        print(f"\nErreur capturée : {e}")