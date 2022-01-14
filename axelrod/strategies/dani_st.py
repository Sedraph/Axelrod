from axelrod.action import Action, actions_to_str
from axelrod.player import Player
from axelrod.strategy_transformers import (
    FinalTransformer,
    TrackHistoryTransformer,
)
import 
import numpy as np

C, D = Action.C, Action.D

class dani_st(Player):

    def __init__(self):
        AB = []
    def strategy(self, opponent, AB):

        X = 0

        if not self.history:
            return C

        if self.history[-1] == 'C':
            if opponent.history[-1] == 'C':
                X = 0
            else:
                X = 1
        else:
            if opponent.history[-1] == 'C':
                X = 2
            else:
                X = 3

        SOL = np.random.uniform(0,1)

        if SOL < AB[X]:
            return C
        else:
            return D

