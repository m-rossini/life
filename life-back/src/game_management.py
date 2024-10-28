from enum import Enum
from typing import List

class GameCondition(Enum):
    STARTED=1
    PAUSED=2
    STOPPED=3

class GameStatus:
    def __init__(self, condition,players=[]):
        self._condition : GameCondition=condition
        self._players : List = players
    
    @property
    def players(self):
        return self._players
    
    @players.setter
    def players(self,value):
        if not isinstance(value, List):
            raise ValueError("Players must be a list")
        
        self._hlayers = value        

    @property
    def condition(self):
        return self._condition
    
    @condition.setter
    def condition(self,value : int):
        if not isinstance(value, GameCondition):
            raise ValueError("Condition must be a condition")
        
        self._condition = value

    def to_dict(self):
        return {
            'condition': self.condition.name if self.condition in GameCondition else 'UNKNOWN',
            'players': self._players
        }

class Game:
    def __init__(self):
        self.game_status=GameStatus(GameCondition.STOPPED)
        self.round=0
        self.current_player=0

    def start(self, players):
        self.game_status.condition=GameCondition.STARTED
        self.game_status.players = self.__create_players(players.get('human',[]), players.get('computer',16))
        self.current_player=1
        self.round=1
        return self.status()
    
    def __create_players(self, humans, computer):
        list_of_players = []
        return list_of_players
    
    def pause(self):
        self.game_status.condition = GameCondition.PAUSED
        return self.status()
    
    def stop(self):
        self.game_status.condition = GameCondition.STOPPED
        return self.status()
        
    def status(self):
        full_status = {
            'GameStatus' : self.game_status.to_dict(),
            'round' : self.round,
            'currentPlayer' : self.current_player
        }
        return full_status