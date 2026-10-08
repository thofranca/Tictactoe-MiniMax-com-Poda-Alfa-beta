import random
from tictactoe import *

def random_choice(state):
    return random.choice(actions(state))