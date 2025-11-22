# -*- coding: utf-8 -*-

class Contact:
    def __init__(self, nom: str, telephone: str, email: str):
        self.nom = nom
        self.telephone = telephone
        self.email = email
    
    @property
    def initiale(self):
        return self.nom[0].upper()


class Carnet:
    def __init__(self):
        self._contacts = []                     # attribut privé
    
    def ajouter(self, contact: Contact):
        self._contacts.append(contact)
    
    def recherche(self, fragment: str):
        frag = fragment.lower()
        return [c for c in self._contacts if frag in c.nom.lower()]
    
    def afficher_tous(self):
        for c in self._contacts:
            print(f"{c.nom} – {c.telephone} – {c.email}")
    
    @property
    def nombre_contacts(self):
        return len(self._contacts)


# Démonstration (lance le fichier et ça s'exécute)
if __name__ == "__main__":
    c = Carnet()
    
    c.ajouter(Contact("Amina Saidi",      "0612345678", "amina@example.com"))
    c.ajouter(Contact("Youssef Belkhou",  "0699988777", "youssef@example.com"))
    c.ajouter(Contact("Said Toumi",       "0677801122", "said@example.com"))
    
    print("Tous les contacts :")
    c.afficher_tous()
    print()
    
    print("Recherche avec 'sa' :")
    resultat = c.recherche("sa")
    for contact in resultat:
        print(contact.nom, contact.telephone)
    
    print()
    print(f"Nombre total de contacts : {c.nombre_contacts}")
    print(f"Initiale du premier contact : {c._contacts[0].initiale}")