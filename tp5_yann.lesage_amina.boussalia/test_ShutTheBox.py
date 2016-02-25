#Amina boussalia
#Yann Lesage

from ShutTheBox import *
import unittest
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
        self.assertTrue(1<=res and res<=6)

    def test_random_in_good_range_and_can_generate_other_number_than_1_succes(self):
        dice= Dice(6)
        res= dice.launch()
        self.assertTrue(1<=res and res<=6)

class TestPlayer(unittest.TestCase):
    def test_launch_one_dice_failure_cannot_launch_3_dice(self):
        dice= mock()
        board= mock()
        player= Player(dice,board)
        self.assertRaises(InvalidNumberOfDiceError,
                          player.launchDice,
                          3)

    
    def test_launch_one_dice_failure_cannot_launch_0_dice(self):
        dice= mock()
        board= mock()
        player= Player(dice,board)
        self.assertRaises(InvalidNumberOfDiceError,
                          player.launchDice,
                          0)

    def test_launch_one_dice_failure_7_8_9_not_used(self):
        dice= mock()
        board= mock()
        when(board).canLaunchOneDice().thenReturn(False)
        player= Player(dice,board)
        self.assertRaises(InvalidNumberOfDiceError,
                          player.launchDice,
                          1)

    def test_launch_one_dice_succes_7_8_9_used(self):
        dice_result=3
        dice= mock()
        when(dice).launch().thenReturn(dice_result)
        board= mock()
        when(board).canLaunchOneDice().thenReturn(True)
        player= Player(dice,board)
        self.assertEquals(dice_result, player.launchDice(1))

    def test_launch_two_dices_succes(self):
        dice_result_one=3
        dice_result_two=2
        dice_result=5
        dice= mock()
        when(dice).launch().thenReturn(dice_result_one).thenReturn(dice_result_two)
        board= mock()
        when(board).canLaunchOneDice().thenReturn(True)
        player= Player(dice,board)
        self.assertEquals(dice_result, player.launchDice(2))

    def test_selectNumberDice_uselesstest_just_to_have_100_pourcent_succes(self):
        dice= mock()
        board= mock()
        player= Player(dice,board)
        self.assertEquals(2, player.selectNumberDice(2))
    
#class TestHumanPlayer(unittest.TestCase):
    
