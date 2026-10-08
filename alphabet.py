from tictactoe import *
from minimax import min_value, max_value
import minimax

def alphabeta(state, player):
    if terminal(state):
        return None
    
    minimax.estados_expandidos += 1
    
    alpha = float('-inf')
    beta = float('inf')
    
    if player == 'X':
        melhor_v = float('-inf')
        acao = None
        for action in actions(state):
            v = min_value(result(state, action, player), 'O', usa_poda=True, alpha=alpha, beta=beta)
            if v > melhor_v:
                melhor_v = v
                acao = action
            alpha = max(alpha, melhor_v)
        return acao
    else:
        melhor_v = float('inf')
        acao = None
        for action in actions(state):
            v = max_value(result(state, action, player), 'X', usa_poda=True, alpha=alpha, beta=beta)
            if v < melhor_v:
                melhor_v = v
                acao = action
            beta = min(beta, melhor_v)
        return acao
