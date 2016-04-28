class TestJeuDevinerUnNombre(unittest.TestCase):
    def test_win_first_try_succes(self):
        A_DEVINER = 4
        generateur_entre_0_et_9 = mock()
        when(generateur_entre_0_et_9).generer().thenReturn(A_DEVINER)

        lecteur =mock()
        when(lecteur).lire_un_nombre().thenReturn(A_DEVINER)
        
        afficheur=mock()
        
        jeu = jeu(generateur_entre_0_et_9,lecteur, afficheur)
        jeu.jouer()

        verify(afficheur).notifier_joueur_a_gagne()

    def test_win_three_try_succes(self):
        A_DEVINER = 4
        TROP_PETIT =3
        TROP_GRAND = 5
        generateur_entre_0_et_9 = mock()
        when(generateur_entre_0_et_9).generer().thenReturn(A_DEVINER)

        lecteur =mock()
        when(lecteur).lire_un_nombre().thenReturn(TROP_PETIT).thenReturn(TROP_GRAND).thenReturn(A_DEVINER)
        
        afficheur=mock()
        
        jeu = jeu(generateur_entre_0_et_9,lecteur, afficheur)
        jeu.jouer()

        verify(afficheur).notifier_joueur_a_gagne()


class TestLecteur(unittest.TestCase):
    def test_nombre_retourner_correspond_a_entree(self):
        flot_entree= io.StringIO("5\n")
        lecteur= LecteurSurEntreeStandart(flot_entree)
        self.assertEqual(lecteur.lire_un_nombre(),5)

class TestIntegration(unittest.TestCase):
    def test_joueur_avec_vrai_lecteur
