import json
from enum import Enum

class GameCondition(Enum):
    STARTED=1
    PAUSED=2
    STOPPED=3

class GameStatus:
    def __init__(self, condition, players=0):
        self._condition : GameCondition=condition
        self._players : int =players
    
    @property
    def players(self):
        return self._players
    
    @players.setter
    def players(self,value):
        if not isinstance(value, int):
            raise ValueError("Players must be an int")
        
        multiplier=1
        if value < 0:
            multiplier=-1
        self._players = value * multiplier        

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
            'players': self.players
        }

class Game:
    def __init__(self):
        self.game_status=GameStatus(GameCondition.STOPPED,players=0)
        self.round=0
        self.current_player=0

    def start(self, players : int=16):
        self.game_status.condition=GameCondition.STARTED
        self.game_status.players=players
        self.current_player=1
        self.round=1
        return self.status()
    
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