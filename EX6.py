# convertisseur.py

class Convertisseur:
    taux_eur_dh = 10.9

    @classmethod
    def mettre_a_jour_taux(cls, nv_taux: float):
        cls.taux_eur_dh = nv_taux

    @staticmethod
    def vers_dh(euros: float) -> float:
        return euros * Convertisseur.taux_eur_dh

    @staticmethod
    def vers_eur(dirhams: float) -> float:
        return dirhams / Convertisseur.taux_eur_dh


# Test / Démo
if __name__ == "__main__":
    montant = 100

    print("Avant mise à jour :", Convertisseur.vers_dh(montant))
    # → 1090.0

    Convertisseur.mettre_a_jour_taux(11.2)

    print("Après mise à jour :", Convertisseur.vers_dh(montant))
    # → 1120.0

    print("1000 DH →", Convertisseur.vers_eur(1000), "€")
    # → environ 89.29 €