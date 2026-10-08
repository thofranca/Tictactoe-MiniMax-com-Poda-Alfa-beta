from tictactoe import *

def minimax(state, player, contador=None):
    if terminal(state):
        return None, None
    
    if contador is not None:
        contador[0] += 1
    
    if player == 'X':
        melhor_v = float('-inf')
        acao = None
        for action in actions(state):
            v = min_value(result(state, action, player), 'O', contador=contador)
            if v > melhor_v:
                melhor_v = v
                acao = action
        return acao, melhor_v
    else:
        melhor_v = float('inf')
        acao = None
        for action in actions(state):
            v = max_value(result(state, action, player), 'X', contador=contador)
            if v < melhor_v:
                melhor_v = v
                acao = action
        return acao, melhor_v

def max_value(state, player, usa_poda=False, alpha=float('-inf'), beta=float('inf'), contador=None):
    if terminal(state):
        return utility(state)
    
    if contador is not None:
        contador[0] += 1
        
    v = float('-inf')
    for action in actions(state):
        v = max(v, min_value(result(state, action, player), 'O', usa_poda, alpha, beta, contador))
        if usa_poda:
            alpha = max(alpha, v)
            if alpha >= beta:
                break
    return v

def min_value(state, player, usa_poda=False, alpha=float('-inf'), beta=float('inf'), contador=None):
    if terminal(state):
        return utility(state)
        
    if contador is not None:
        contador[0] += 1
        
    v = float('inf')
    for action in actions(state):
        v = min(v, max_value(result(state, action, player), 'X', usa_poda, alpha, beta, contador))
        if usa_poda:
            beta = min(beta, v)
            if alpha >= beta:
                break
    return v