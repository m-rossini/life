import json
from enum import Enum
from typing import List
from player import HumanPlayer, ComputerPlayer

class GameCondition(Enum):
    STARTED=1
    PAUSED=2
    STOPPED=3

class GameStatus:
    def __init__(self, condition, players=[]):
        self._condition : GameCondition=condition
        self._players : List = players
        self._round : int=0
        self._current_player : int =0
        self._total_players = len(players)
    
    @property
    def players(self):
        return self._players
    
    @players.setter
    def players(self,value):
        if not isinstance(value, List):
            raise ValueError("Players must be a list")
        
        self._players = value 
        self._total_players = len(value)       

    @property
    def condition(self):
        return self._condition
    
    @condition.setter
    def condition(self,value : int):
        if not isinstance(value, GameCondition):
            raise ValueError("Condition must be a condition")
        
        self._condition = value

    @property
    def round(self):
        return self._round
    
    @property
    def current_player(self):
        return self._current_player
    
    def next_round(self):
        self._round += 1
        #for each player call assess and then play

    def to_dict(self):
        serialized_players = [ single_player.__dict__ for single_player in self._players]
        return {
            'condition': self.condition.name if self.condition in GameCondition else 'UNKNOWN',
            'players': serialized_players,
            'total_players' : self._total_players,
            'round' : self.round,
            'current_player' : self.current_player
        }

class Game:
    def __init__(self):
        self.game_status=GameStatus(GameCondition.STOPPED)

    def start(self, players):
        self.game_status.condition=GameCondition.STARTED
        self.game_status.players = self.__create_players(players.get('human',[]), players.get('computer',16))
        #self.game_status.next_player()
        self.game_status.next_round()
        return self.status()
    
    def __create_players(self, humans, computer):
        return [HumanPlayer(name) for name in humans] + [ComputerPlayer(self.__generate_name(index)) for index in range(1,computer)]
    
    def __generate_name(self,index):
        #TODO Generate a decent name
        return str(index)
    
    def pause(self):
        self.game_status.condition = GameCondition.PAUSED
        return self.status()
    
    def stop(self):
        self.game_status.condition = GameCondition.STOPPED
        return self.status()
        
    def status(self):
        full_status = {
            'GameStatus' : self.game_status.to_dict(),
        }

        return full_status