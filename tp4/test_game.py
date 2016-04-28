class TestGame(unittest.TestCase):
    def test_win_alrealdy_used_fail(self):
        data=mock()
        when(data).exist('erreur').thenReturn(True)
        creator = LoginCreator(data)
        self.assertRaises(AlreadyUsedError,
                          creator.create_login,
                          'test',
                          'aLaCon',
                          'erreur')
