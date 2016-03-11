class Jeu:
    def __init__(self, generateur, lecteur, afficheur):
        self. generateur = generateur 
        self.lecteur= lecteur
        self.afficheur=afficheur

    def jouer(self):
        a_deviner = generateur.generer()
        gagner = false
        while(!gagner):
            self.afficheur.notify_invitation_choisir_un_nombre()
            self.afficheur.notifier_joueur_a_gagne()
            

class LecteurSurEntreeStandart:
    def __init__(self, flux=sys.stdin):
        self.flot_entree = flux

    def lire_un_nombre():
        return int(self.flot_entree.readline())
