#Amina boussalia
#Yann Lesage

from random import *

class NumberAlreadyUsedError(Exception):
    pass

class InvalidNumberOfDiceError(Exception):
    pass

class Board:
    def __init__(self):
        self._numbers=[True]*9

    def _searchOneCombinate(self,actualValue, actualNumber,valueTarget):
        res =[]
        actualValue+=actualNumber
        if actualValue== valueTarget:
            return [[actualNumber]]
        for number in range(actualNumber+1, 10):
            if self._numbers[number-1]:
                if (number+actualValue==valueTarget):
                    res.append([number,actualNumber])
                elif (number+actualValue>valueTarget):
                    break
                else:
                    for combi in self._searchOneCombinate(actualValue,number,valueTarget):
                        combi.append(actualNumber)
                        res.append(combi)
        return res
    
    def searchCombination(self,valueTarget):
        res =[]
        for number in range(1,10):
            if self._numbers[number-1]:
                for combi in self._searchOneCombinate(0, number,valueTarget):
                    res.append(combi)
        return res

    
    def use(self, combination):
        for number in combination:
            if self._numbers[number-1]:
                self._numbers[number-1]=False
            else:
                raise NumberAlreadyUsedError()

    def canLaunchOneDice(self):
        return not(self._numbers[6] and self._numbers[7] and self._numbers[8])

    def score(self):
        res=0
        for number in range(1,10):
            if self._numbers[number-1]:
                res+= number
        return res

class Dice:
    def __init__(self, maxValue):
        self._min =1
        self._max=maxValue
        

    def launch(self):
        return randint(self._min, self._max)

class Player:
    def __init__(self, dice, board):
        self._dice=dice
        self._board=board

    def _launchOneDice(self):
        if self._board.canLaunchOneDice():
            return self._dice.launch()
        else:
            raise InvalidNumberOfDiceError()

    def _launchTwoDice(self):
        return self._dice.launch()+self._dice.launch()
        
    """need to be overwritting to give an IA or to give 
       at player the capacity to choose between one or two dice
       outputStream is used to give return to interface""" 
    def selectNumberDice(self, outputStream):
        return 2
        
    def launchDice(self,numberDice):
        if(numberDice==1):
            return self._launchOneDice()
        elif (numberDice==2):
            return self._launchTwoDice()
        else :
            raise InvalidNumberOfDiceError()

#def HumanPlayer(Player):
    #def chooseCombination(self):

    #def score()

    #def launchDice(number)

    
