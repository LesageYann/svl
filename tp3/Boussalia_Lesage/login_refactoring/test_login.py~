from login import LoginCreator, AlreadyUsedError, ToLongLoginError,NoMinASCIIError,NeedAdminDecisionForLoginError
import unittest
from mockito import *

class TestLoggingManuel(unittest.TestCase):
    def test_login_alrealdy_used_fail(self):
        data=mock()
        when(data).exist('erreur').thenReturn(True)
        creator = LoginCreator(data)
        self.assertRaises(AlreadyUsedError,
                          creator.create_login,
                          'test',
                          'aLaCon',
                          'erreur')

    def test_login_to_long_fail(self):
        data=mock()
        creator = LoginCreator(data)
        self.assertRaises(ToLongLoginError,
                          creator.create_login,
                          'test',
                          'aLaCon',
                          'testtestt')
        
    def test_bound_login_not_to_long_8(self):
        data=mock()
        user=mock()
        user.login="testtest"
        when(data).exist('testtest').thenReturn(False)
        when(data).createUser('testtest','test','vide').thenReturn(user)
        creator = LoginCreator(data)
        self.assertEqual('testtest', creator.create_login('test','vide','testtest').login)

    def test_login_succes(self):
        data=mock()
        user = mock()
        when(data).exist('test').thenReturn(False)
        when(data).createUser('test','test','vide').thenReturn(user)
        creator = LoginCreator(data)
        self.assertEqual(user, creator.create_login('test','vide','test'))

    def test_minuscule_ASCII_echec_number(self):
        data=mock()
        creator = LoginCreator(data)
        self.assertRaises(NoMinASCIIError,
                          creator.create_login,
                          'test',
                          'aLaCon',
                          'test22')

    def test_minuscule_ASCII_echec_maj(self):
        data=mock()
        creator = LoginCreator(data)
        self.assertRaises(NoMinASCIIError,
                          creator.create_login,
                          'test',
                          'aLaCon',
                          'testTT')


class TestCalculeLogin(unittest.TestCase):
    def test_new_login_has_8_char_max_first_try(self):
        data=mock()
        creator = LoginCreator(data)
        self.assertEqual("namename",creator.calculate_new_login("namenamename","test"))

    def test_new_login_has_8_char_max_second_try(self):
        data=mock()
        creator = LoginCreator(data)
        self.assertEqual("namenamt",creator.calculate_new_login("namenamename","test",True))

class TestAutomatiqueCreateLogin(unittest.TestCase):
    def test_automatique_mode_succes_valid_login_first_try(self):
        data=mock()
        creator = LoginCreator(data)
        user = mock()
        when(data).exist('loginlog').thenReturn(False)
        when(data).createUser('loginlog','loginlogin','vide').thenReturn(user)
        self.assertEqual(user, creator.create_login_auto('loginlogin','vide'))

    def test_automatique_mode_succes_valid_login_second_try(self):
        data=mock()
        creator = LoginCreator(data)
        user = mock()
        when(data).exist('loginlog').thenReturn(True)
        when(data).exist('loginlov').thenReturn(False)
        when(data).createUser('loginlov','loginlogin','vide').thenReturn(user)
        self.assertEqual(user, creator.create_login_auto('loginlogin','vide'))

    def test_automatique_mode_fail_two_first_login_already_exist(self):
        data=mock()
        creator = LoginCreator(data)
        user = mock()
        when(data).exist('loginlog').thenReturn(True)
        when(data).exist('loginlov').thenReturn(True)
        self.assertRaises(NeedAdminDecisionForLoginError,
                          creator.create_login_auto,
                          'loginlogin',
                          'vide')
        
    def test_automatique_mode_fail_nonMinASCII(self):
        data=mock()
        creator = LoginCreator(data)
        user = mock()
        self.assertRaises(NoMinASCIIError,
                          creator.create_login_auto,
                          'lR5oginlogin',
                          'vide') 
    
