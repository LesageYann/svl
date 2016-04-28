import unittest
from mockito import *

class TestEmprunterUnLivre(unittest.TestCase):

    def test_livre_consultable_uniquement_echec_emprunt(self):
        fabrique = mock()
        livre=mock()
        membre = mock()
        livre.empruntable= false
        serviceEmprunts = ServiceEmprunts(fabrique)
        self assertRaises(LivreNonEmpruntableError, serviceEmprunts.emprunter, livre,membre)

    def test_membre_quota_atteint_echec_emprunt(self):
        fabrique = mock()
        livre=mock()
        livre.empruntable= true
        membre = mock()
        when(membre).peutEmprunter().thenReturn(false)
        serviceEmprunts = ServiceEmprunts(fabrique)
        self assertRaises(QuotaAtteintError, serviceEmprunts.emprunter, livre, membre)

    def test_emprunt_reussi(self):
        fabrique = mock()
        livre=mock()
        livre.empruntable= true
        membre = mock()
        when(membre).peutEmprunter().thenReturn(false)
        serviceEmprunts = ServiceEmprunts(fabrique)
        emprunt= serviceEmprunts.emprunter(livre, membre)
        assert.Equal
        
