from tictactoe import *

estados_expandidos = 0

def minimax(state, player):
    global estados_expandidos
    if terminal(state):
        return None
    
    estados_expandidos += 1
    
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

def max_value(state, player, usa_poda=False, alpha=float('-inf'), beta=float('inf')):
    global estados_expandidos
    if terminal(state):
        return utility(state)
    estados_expandidos += 1
    v = float('-inf')
    for action in actions(state):
        v = max(v, min_value(result(state, action, player), 'O', usa_poda, alpha, beta))
        if usa_poda:
            alpha = max(alpha, v)
            if alpha >= beta:
                break
    return v

def min_value(state, player, usa_poda=False, alpha=float('-inf'), beta=float('inf')):
    global estados_expandidos
    if terminal(state):
        return utility(state)
    estados_expandidos += 1
    v = float('inf')
    for action in actions(state):
        v = min(v, max_value(result(state, action, player), 'X', usa_poda, alpha, beta))
        if usa_poda:
            beta = min(beta, v)
            if alpha >= beta:
                break
    return v