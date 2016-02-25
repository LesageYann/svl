#Amina boussalia
#Yann Lesage

from random import *
import time

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
    def __init__(self, dice, board, name):
        self._dice=dice
        self._board=board
        self.name=name

    def _launchOneDice(self):
        if self._board.canLaunchOneDice():
            return self._dice.launch()
        else:
            raise InvalidNumberOfDiceError()

    def _launchTwoDice(self):
        return self._dice.launch()+self._dice.launch()
        
    """need to be overwritting to give an IA or to give 
       at player the capacity to choose between one or two dice
       to ask interface or player to choose, set the return to None""" 
    def selectNumberDice(self):
        return 2

    def getScore(self):
        return this._board.score()
        
    def launchDice(self,numberDice):
        diceValue=0
        if(numberDice==1):
            diceValue= self._launchOneDice()
        elif (numberDice==2):
            diceValue= self._launchTwoDice()
        else :
            raise InvalidNumberOfDiceError()
        return (diceValue, self._board.searchCombination(diceValue))

    def useCombination(self, combination):
        self._board.use(combination)

    
class GameMotor:
    """inputStream and outputStream need to create by the interface who need to use the game motor
        for inputStream and outputStream wait an object like StringIO
        you to separate in two thread the game and the interface"""
    def __init__(self, inputStream, outputStream, maxTurn, players):
        self._input=inputStream
        self._output=outputStream
        self._maxTurn=maxTurn
        self._turn=0
        self._ingame=True
        self._players= players

    def _waitInput(self):
        while(True):
            content=self._input.readline()
            if(content != ""):
                return content[:-1]
            time.sleep(0.5)

    def _waitArray(self):
        tmp= self._waitInput()[1:-1].split(',')
        return tmp

    def DisplayScoreEndGame():
        self._ingame=False
        winner= ""
        minScore=100
        for player in self._players:
            tmpScore= player.getScore()
            if tmpScore < minScore :
                minScore=tmpScore
                winner= player.name
            self._output.write("Score "+player.name + " "+ tmpScore)
        self._output.write("Winner "+winner)
    
    def play(self):
        while(self._ingame==True):
            playOneTurn()
        
    def playOneTurn(self):
        self._turn+=1
        if self._turn== self._maxTurn :
            self.DisplayScoreEndGame()
        else :
            for player in self._players:
                self._output.write("StartTurn "+player.name)
                numberDices=player.selectNumberDice()
                if(numberDices==None):
                    #if the number dice is not auto
                    self._output.write("SelectNumberDice ")
                    numberDices= self._waitInput()
                try:
                    diceValue,combination = player.launchDice(numberDices)
                    self._ouput.write("Launched "+diceValue+" "+combination)
                    combinationSelected = self._waitArray()
                    if(combination!=None):
                        player.useCombination(combinationSelected)
                        self._output.write("CombinationUsed ")
                except NumberAlreadyUsedError:
                    self._output.write("BadCombination")
                except InvalidNumberOfDiceError:
                    self._output.write("CanLaunchDice "+numberDices)
                if(player.getScore()==0):
                    self.DisplayScoreEndGame()
                else:
                    self._output.write("EndTurn "+player.name)
