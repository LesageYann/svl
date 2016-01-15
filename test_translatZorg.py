"""
Application bancaire : comptes
"""

import unittest

class TestTranslatZorg(unittest.TestCase):

    def test_conserve_longueur(self):
        entre="mon test"
        sortie=tranlatZorg(entre)
        self.assertEqual(len(entre),len(sortie))

    def test_reverse_one_word(self):
        entre= "test"

