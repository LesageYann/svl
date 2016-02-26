from selenium import webdriver
import unittest
from calculateur import CalculateurPoids

class TestPageAccueil(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.navigateur = webdriver.Firefox()
        cls.navigateur.get('http://localhost:8080')

    @classmethod
    def tearDownClass(cls):
        cls.navigateur.quit()
        
    def test_la_page_a_un_titre(self):
        titre = self.navigateur.title
        self.assertEqual(titre, "accueil")

    def test_la_page_contient_un_form_avec_action_correct(self):
        self.lien = self.navigateur.find_element_by_id('calculateur')
        url = self.lien.get_attribute('action')
        self.assertEqual(url, "http://localhost:8080/resultat")

    def test_le_form_calculateur_contient_une_boite_de_saisie_numerique(self):
        self.navigateur = webdriver.Firefox()
        self.navigateur.get('http://localhost:8080')
        self.boite = self.navigateur.find_element_by_id('taille')
        type = self.boite.get_attribute('type')
        self.navigateur.quit()
        self.assertEqual("number", type)



class TestPageResultat(unittest.TestCase):
    def test_la_page_a_un_titre(self):
        navigateur = webdriver.Firefox()
        navigateur.get('http://localhost:8080/resultat')
        titre = navigateur.title
        navigateur.quit()
        self.assertEqual(titre, "resultat")

    def test_la_page_renvoie_erreur_taille_vide(self):
        navigateur = webdriver.Firefox()
        navigateur.get('http://localhost:8080/resultat')
        elem = self.navigateur.find_element_by_id('erreurpoids')
        navigateur.quit()
        self.assertEqual(elem.text  , "erreur taille vide")

    def test_la_page_renvoie_erreur_taille_vide(self):
        navigateur = webdriver.Firefox()
        navigateur.get('http://localhost:8080/resultat?taille=1yt0&nom=envoyer')
        elem = navigateur.find_element_by_id('erreurpoids')
        navigateur.quit()
        self.assertEqual(elem.text  , "erreur taille invalie")

    def test_la_page_renvoie_bon_poids(self):
        navigateur = webdriver.Firefox()
        navigateur.get('http://localhost:8080/resultat?taille=190&nom=envoyer')
        elem = navigateur.find_element_by_id('poids')
        navigateur.quit()
        self.assertEqual(elem.text  , "80.0")


class TestCalulateurPoids(unittest.TestCase):
    def test_retour_bon_poids(self):
        calculateur = CalculateurPoids()
        self.assertEquals(calculateur.calculPoids("190"), 80.0)

    
    def test_retour_erreur_format_invalid(self):
        calculateur = CalculateurPoids()
        self.assertRaises(ValueError, calculateur.calculPoids, "troll")
