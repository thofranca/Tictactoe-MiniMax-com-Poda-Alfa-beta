from tictactoe import *

def minimax(state, player):
    if terminal(state):
        return None
    
    if player == 'X':
        melhor_v = float('-inf')
        acao = None
        for action in actions(state):
            v = min_value(result(state, action, player), 'O')
            if v > melhor_v:
                melhor_v = v
                acao = action
        return acao
    else:
        melhor_v = float('inf')
        acao = None
        for action in actions(state):
            v = max_value(result(state, action, player), 'X')
            if v < melhor_v:
                melhor_v = v
                acao = action
        return acao

def max_value(state, player):
    if terminal(state):
        return utility(state)
    v = float('-inf')
    for action in actions(state):
        v = max(v, min_value(result(state, action, player), 'O'))
    return v

def min_value(state, player):
    if terminal(state):
        return utility(state)
    v = float('inf')
    for action in actions(state):
        v = min(v, max_value(result(state, action, player), 'X'))
    return v