from login import *
import unittest
from mockito import *

class TestLoggingManuel(unittest.TestCase):
    def test_login_alrealdy_used_fail(self):
        data=mock()
        verif = mock()
        when(verif).allVerify('erreur').thenReturn(True)
        when(data).exist('erreur').thenReturn(True)
        creator = LoginCreator(data, verif)
        self.assertRaises(AlreadyUsedError,
                          creator.create_login,
                          'test',
                          'aLaCon',
                          'erreur')

    def test_login_succes(self):
        data=mock()
        user = mock()
        verif = mock()
        when(verif).allVerify('test').thenReturn(True)
        when(data).exist('test').thenReturn(False)
        when(data).createUser('test','test','vide').thenReturn(user)
        creator = LoginCreator(data,verif)
        self.assertEqual(user, creator.create_login('test','vide','test'))
    

class TestValidLogin(unittest.TestCase):
    def test_login_to_long_fail(self):
        verif = LoginVerify()
        self.assertRaises(ToLongLoginError,
                          verif.allVerify,
                          'testtestt')
        
    def test_bound_login_not_to_long_8(self):
        verif = LoginVerify()
        self.assertTrue(verif.allVerify('testtest'))

    def test_minuscule_ASCII_echec_number(self):
        verif = LoginVerify()
        self.assertRaises(NoMinASCIIError,
                          verif.allVerify,
                          'test22')

    
    def test_minuscule_ASCII_echec_maj(self):
        verif = LoginVerify()
        self.assertRaises(NoMinASCIIError,
                          verif.allVerify,
                          'testTT')

class TestCalculeLogin(unittest.TestCase):
    def test_new_login_has_8_char_max_first_try(self):
        verif = LoginVerify()
        self.assertEqual("namename",verif.calculate_new_login("namenamename","test"))

    def test_new_login_has_8_char_max_second_try(self):
        verif = LoginVerify()
        self.assertEqual("namenamt",verif.calculate_new_login("namenamename","test",True))

class TestAutomatiqueCreateLogin(unittest.TestCase):
    def test_automatique_mode_succes_valid_login_first_try(self):
        data=mock()
        verif = mock()
        when(verif).allVerify('loginlog').thenReturn(True)
        when(verif).calculate_new_login('loginlogin','vide',False).thenReturn('loginlog')
        creator = LoginCreator(data,verif)
        user = mock()
        when(data).exist('loginlog').thenReturn(False)
        when(data).createUser('loginlog','loginlogin','vide').thenReturn(user)
        self.assertEqual(user, creator.create_login_auto('loginlogin','vide'))

    def test_automatique_mode_succes_valid_login_second_try(self):
        data=mock()
        verif = mock()
        when(verif).allVerify('loginlov').thenReturn(True)
        when(verif).calculate_new_login('loginlogin','vide',False).thenReturn('loginlog')
        when(verif).calculate_new_login('loginlogin','vide',True).thenReturn('loginlov')
        creator = LoginCreator(data,verif)
        user = mock()
        when(data).exist('loginlog').thenReturn(True)
        when(data).exist('loginlov').thenReturn(False)
        when(data).createUser('loginlov','loginlogin','vide').thenReturn(user)
        self.assertEqual(user, creator.create_login_auto('loginlogin','vide'))

    def test_automatique_mode_fail_two_first_login_already_exist(self):
        data=mock()
        verif = mock()
        when(verif).allVerify('loginlov').thenReturn(True)
        when(verif).calculate_new_login('loginlogin','vide',True).thenReturn('loginlov')
        creator = LoginCreator(data,verif)
        user = mock()
        when(data).exist('loginlov').thenReturn(True)
        self.assertRaises(NeedAdminDecisionForLoginError,
                          creator.create_login_auto,
                          'loginlogin',
                          'vide',
                           True)
        
    def test_automatique_mode_fail_nonMinASCII(self):
        data=mock()
        verif = mock()
        when(verif).allVerify('lR5oginl').thenRaise(NoMinASCIIError)
        when(verif).calculate_new_login('lR5oginlogin','vide',False).thenReturn('lR5oginl')
        creator = LoginCreator(data,verif)
        user = mock()
        self.assertRaises(NoMinASCIIError,
                          creator.create_login_auto,
                          'lR5oginlogin',
                          'vide') 
    
