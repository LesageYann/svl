"""
Application bancaire : comptes
"""

class Compte():
    """
    Représentation d'un compte bancaire.
    """

    def __init__(self):
        """Cree un compte avec solde nul."""
        self.solde = 0.0

    def crediter(self, montant):
        if montant <= 0:
            raise NegatifCreditError()
        self.solde += montant

        
    def debiter(self, montant):
        if montant <= 0:
            raise NegatifCreditError()
        self.solde -= montant
        
class NegatifCreditError(Exception):
    pass

class NegatifAtCreateError(Exception):
    pass
