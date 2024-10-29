from abc import abstractmethod
from enum import Enum

import namesgenerator

class Playe_Type(Enum):
    HUMAN = "Human"
    COMPUTER = "Computer"

class Player:
    def __init__(self):
        pass
    
    @abstractmethod
    def name(self):
        pass
    
    @abstractmethod
    def play(self):
        self

class ComputerPlayer(Player):
    def __init__(self, name):
        self.name  = namesgenerator.get_random_name()
        self.type = Playe_Type.COMPUTER.value
     
    def name(self):
        return self.name
    
    def play(self):
        print(f"Computer Player {self.name} playing")

class HumanPlayer(Player):
    def __init__(self, name):
        self.name = name
        self.type = Playe_Type.HUMAN.value

    def name(self):
        return self.name
    
    def play(self):
        print(f"Human Player {self.name} playing")    