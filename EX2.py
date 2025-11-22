class CompteurPage:
    total_visites = 0
    
    def __init__(self, url: str):
        self.url = url
        self.visites_par_page = 0
        CompteurPage.total_visites += 1
        self.enregistrer_lecture()
    
    def enregistrer_lecture(self):
        self.visites_par_page += 1
    
    def afficher_stats(self) -> str:
        return f"Page {self.url} - visites globales : {CompteurPage.total_visites} | visites cette page : {self.visites_par_page}"

# Test
p1 = CompteurPage("https://example.com")
p2 = CompteurPage("https://example.com/blog")
p3 = CompteurPage("https://example.com/contact")

p1.enregistrer_lecture()
p1.enregistrer_lecture()
p3.enregistrer_lecture()

for p in [p1, p2, p3]:
    print(p.afficher_stats())
