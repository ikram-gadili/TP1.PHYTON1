# -*- coding: utf-8 -*-

class Article:
    def __init__(self, reference: str, designation: str, prix_ht: float, stock: int = 0):
        self.reference = reference
        self.designation = designation
        self.prix_ht = prix_ht
        self.stock = stock

    def valeur_stock(self) -> float:
        return self.prix_ht * self.stock

    def __str__(self) -> str:
        return f"Réf {self.reference} – {self.designation} : {self.stock} unités à {self.prix_ht} € HT"

    def approvisionner(self, qte: int):
        self.stock += qte
        with open("mouvements.log", "a", encoding="utf-8") as f:
            f.write(f"+{qte} {self.reference} ({self.designation})\n")


# Création des 3 articles
a1 = Article("REF001", "Clavier mécanique", 75.90, 10)
a2 = Article("REF002", "Souris gamer", 49.50, 25)
a3 = Article("REF003", "Écran 27\"", 299.00, 5)

articles = [a1, a2, a3]

# Affichage demandé
for a in articles:
    print(a)

# Valeur totale du stock
total = sum(a.valeur_stock() for a in articles)
print(f"Valeur d'inventaire : {total:.2f} €")

# Petit test de l'approvisionnement (facultatif)
a1.approvisionner(8)
a3.approvisionner(3)

print("\nAprès approvisionnement :")
print(a1)
print(a3)