#Amina boussalia
#Yann Lesage

from ShutTheBox import *
import unittest,io
from mockito import *

class TestBoard(unittest.TestCase):
    def test_use_number_succes(self):
        board= Board()
        combination= [1,5]
        board.use(combination)
        self.assertFalse(board._numbers[combination[0]-1])
        self.assertFalse(board._numbers[combination[1]-1])

    def test_use_number_already_used_fail_with_error(self):
        board= Board()
        combination= [1,5]
        board.use(combination)
        self.assertRaises(NumberAlreadyUsedError,
                          board.use,
                          combination)

    def test_search_combination_exist_all_number_not_used_succes(self):
        board= Board()
        combination =[[5,2,1],[4,3,1],[7,1],[6,2],[5,3],[8]]
        self.assertEquals(combination,board.searchCombination(8))

    def test_search_combination_exist_number_already_used_succes(self):
        board= Board()
        board.use([1,2,3,9])
        board.use([4,8])
        combination =[[7,5]]
        self.assertEquals(combination,board.searchCombination(12))

    def test_can_launch_one_dice_true_7_8_9_used_succes(self):
        board= Board()
        board.use([3,9])
        board.use([7,8])
        self.assertTrue(board.canLaunchOneDice())

    def test_score_succes(self):
        board= Board()
        board.use([3,9])
        board.use([7,8])
        self.assertEquals(18,board.score())

    def test_score_all_number_used_succes(self):
        board= Board()
        board.use([1,2,3,4,5,6,7,8,9])
        self.assertEquals(0,board.score())

    def test_score_all_number_used_succes(self):
        board= Board()
        self.assertEquals(45,board.score())

class TestDice(unittest.TestCase):
    def test_random_in_good_range_generate_always_1_succes(self):
        dice= Dice(1)
        res= dice.launch()
        self.assertTrue(1==res)

    def test_random_in_good_range_and_can_generate_other_number_than_1_succes(self):
        dice= Dice(6)
        res= dice.launch()
        self.assertTrue(1<=res and res<=6)

class TestPlayerLaunchDice(unittest.TestCase):
    def test_launch_one_dice_failure_cannot_launch_3_dice(self):
        dice= mock()
        board= mock()
        player= Player(dice,board,"test")
        self.assertRaises(InvalidNumberOfDiceError,
                          player.launchDice,
                          3)

    
    def test_launch_one_dice_failure_cannot_launch_0_dice(self):
        dice= mock()
        board= mock()
        player= Player(dice,board,"test")
        self.assertRaises(InvalidNumberOfDiceError,
                          player.launchDice,
                          0)

    def test_launch_one_dice_failure_7_8_9_not_used(self):
        dice= mock()
        board= mock()
        when(board).canLaunchOneDice().thenReturn(False)
        player= Player(dice,board,"test")
        self.assertRaises(InvalidNumberOfDiceError,
                          player.launchDice,
                          1)

    def test_launch_one_dice_succes_7_8_9_used(self):
        dice_result=3
        dice= mock()
        when(dice).launch().thenReturn(dice_result)
        board= mock()
        when(board).canLaunchOneDice().thenReturn(True)
        player= Player(dice,board,"test")
        diceValue, combinations =player.launchDice(1)
        self.assertEquals(dice_result, diceValue)

    def test_launch_two_dices_succes(self):
        dice_result_one=3
        dice_result_two=2
        dice_result=5
        dice= mock()
        when(dice).launch().thenReturn(dice_result_one).thenReturn(dice_result_two)
        board= mock()
        when(board).canLaunchOneDice().thenReturn(True)
        player= Player(dice,board,"test")
        diceValue, combinations =player.launchDice(2)
        self.assertEquals(dice_result, diceValue)

    def test_selectNumberDice_uselesstest_just_to_have_100_pourcent_succes(self):
        dice= mock()
        board= mock()
        player= Player(dice,board,"test")
        self.assertEquals(2, player.selectNumberDice())
    
class TestPlayerOtherOperation(unittest.TestCase):
    def test_useCombination_fail_already_used(self):
        dice= mock()
        board= mock()
        when(board).use([7,8]).thenRaise(NumberAlreadyUsedError)
        player= Player(dice,board,"test")
        self.assertRaises(NumberAlreadyUsedError,
                          player.useCombination,
                          [7,8])

    def test_useCombination_succes(self):
        dice= mock()
        board= mock()
        when(board).use([7,8]).thenReturn()
        player= Player(dice,board,"test")
        player.useCombination([7,8])
        verify(board).use([7,8])

class TestGameMotorUtil(unittest.TestCase):
    def test_waitInput_success(self):
        p1= mock()
        p2= mock()
        input=io.StringIO("test\n")
        output=io.StringIO()
        game=GameMotor( input, output, "10", [p1,p2])
        res=game._waitInput()
        self.assertEquals("test",res)

    def test_waitInput_success(self):
        p1= mock()
        p2= mock()
        input=io.StringIO("[5,6,7,8]\n")
        output=io.StringIO()
        game=GameMotor( input, output, "10", [p1,p2])
        res=game._waitArray()
        self.assertEquals(['5','6','7','8'],res)


#Nous n'avons pas réussi a trouver comment corriger l'erreur TypeError: 'AnswerSelector' object is not iterable
#Du coup on a continué l'implémentation de GameMotor pour pouvoir donner les tests qu'il nous reste encore a faire :
#-- faire deux test pour voir les write dans output stream quand on a les erreurs NumberAlreadyUsedError et InvalidNumberOfDiceError
#-- un test pour verifier que le jeu se stop bien avec les bon output
#-- un test pour verifier qu'on ai les bon output lors d'un tour
#-- un test d'intégration avec tous les composants
class TestGameMotor(unittest.TestCase):
    def test_play_one_turn_success_increment_turn(self):
        replaunchDice= (5, [[5],[2,3]])
        p1= mock()
        p1.name="test"
        when(p1).launchDice(2).thenReturn(replaunchDice )
        when(p1).useCombination([5]).thenReturn()
        p2= mock()
        p2.name="test"
        when(p2).launchDice(2).thenReturn( replaunchDice )
        when(p2).useCombination([5]).thenReturn()
        input=io.StringIO("[5]\n[5]\n[5]\n[5]\n[5]\n")
        output=io.StringIO()
        game=GameMotor( input, output, "10", [p1,p2])
        game.playOneTurn()
        self.assertEquals(1,game._turn)

    def test_play_one_turn_success_increment_turnall_player_play(self):
        p1= mock()
        p1.name="test"
        when(p1).launchDice(2).thenReturn( (5, [[5],[2,3]] ))
        when(p1).useCombination([5]).thenReturn()
        p2= mock()
        p2.name="test"
        when(p2).launchDice(2).thenReturn( (5, [[5],[2,3]] ))
        when(p2).useCombination([5]).thenReturn()
        input=io.StringIO("[5]\n[5]\n[5]\n[5]\n[5]\n[5]\n")
        output=io.StringIO()
        game=GameMotor( input, output, "10", [p1,p2])
        game.playOneTurn()
        verify(p1).launchDice(2)
        verify(p2).launchDice(2)
