"""Service d'emprunt d'un livre"""
class ServiceEmprunts:
    def __init__(self, fabrique):
        self.fabriqueEmprunts=fabrique
        

    def emprunter(self, livre, membre):
        """emprunt le livre.
        Si le livre n'est pas disponible a l'emprunt erreur
        Si le membre a atteint son quota erreur
        Sinon l'emprunt se fait :
        - creation de l'emprunt
        - affichage des caractéristique de l'emprunt"""
        if not livre.empruntable:
            raise LivreNonEmpruntableError()
        if not member.peutEmprunter():
            raise QuotaAtteintError()
        return self.fabriqueEmprunts.creerEmprunt(livre,membre)

class LivreNonEmpruntableError(Exception):
    pass

class QuotaAtteintError(Exception):
    pass

class Emprunt:
    pass

class Livre:
    """
    >>>livre =Livre
    >>>livre.emruntable
    True
    """

class membre:
    """
    >>>membre=membre()
    >>>membre.peutEmprunter()
    True
    """
