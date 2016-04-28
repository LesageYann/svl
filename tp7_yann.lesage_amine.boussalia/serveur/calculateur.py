import cherrypy
from string import Template

PAGE_INDEX = """
<html>
<head>
<title>accueil</title>
</head>
<body>
<form id="calculateur" method="get" action="/resultat">
<label>taille(cm)</label>: <input type="number" min="100" max="240" name="taille" id="taille" value=""> 
<INPUT TYPE="submit" NAME="nom" VALUE="envoyer">
</form>
</body>
</html>
"""

PAGE_RESULTAT = """
<html>
<head>
<title>resultat</title>
</head>
<body>
 $poids
</body>
</html>
"""

class CalculateurPoids:
    def calculPoids(self,taille):
           t = float(taille)/100
           return t * 100 - 100 - (t * 100 - 150) / 4

class MonAppli:
    def __init__(self,algo):
        self.page_res= Template(PAGE_RESULTAT)
        self.page_res_bon="votre poids ideal est de <span id=\"poids\">"
        self._algo = algo

    @cherrypy.expose
    def index(self):
        return PAGE_INDEX
    
    @cherrypy.expose
    def resultat(self, taille=None,nom=None):
        dico={}
        if(taille==None or taille==""):
            dico["poids"]= "<span id=\"erreurpoids\">erreur taille vide</span>"
        else :
            try:
                poids= self._algo.calculPoids(taille)
                dico["poids"]= self.page_res_bon + str(poids)+"</span>"
            except ValueError:
                dico["poids"]= "<span id=\"erreurpoids\">erreur taille invalide</span>"
        return self.page_res.safe_substitute(dico)

    def page_resultat_conversion(self, valeur_celsius):
        return PAGE_RESULTAT_ERRONE
        
if __name__ == '__main__':
    cherrypy.quickstart(MonAppli(CalculateurPoids()))


