# journal.py (version corrigée)

from datetime import datetime

class JournalTaches:
    def __enter__(self):
        self.fichier = open("journal.txt", "a", encoding="utf-8")
        return self

    def enregistrer(self, tache: str):
        maintenant = datetime.now().isoformat(timespec="minutes")
        self.fichier.write(f"{maintenant} — {tache}\n")
        self.fichier.flush()

    def __exit__(self, exc_type, exc, tb):
        self.fichier.close()

    def lire(self):
        try:
            with open("journal.txt", "r", encoding="utf-8") as f:
                lignes = f.readlines()
            for ligne in reversed(lignes):
                print(ligne.strip())
        except FileNotFoundError:
            print("Aucune tâche encore.")


# Test
if __name__ == "__main__":
    from time import sleep

    with JournalTaches() as journal:
        journal.enregistrer("Préparer la réunion du projet X")
        sleep(1)
        journal.enregistrer("Faire la revue de code")
        sleep(1)
        journal.enregistrer("Envoyer le rapport hebdomadaire")

    print("\nHistorique (inverse) :")
    journal.lire()