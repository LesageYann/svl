import unittest
from mockito import *

class TestLoggingManuel(unittest.TestCase):
    def test_login_alrealdy_used_fail(self):
        creator = LoginCreator();
        self.assertRaises(AlreadyUsedError,
                          creator.create_login,
                          name,
                          firstName,
                          login)

#        def test_troncat_name(self):
