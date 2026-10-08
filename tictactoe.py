cerquilha = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

def reset_cerquilha(board):
    for i in range(3):
        for j in range(3):
            board[i][j] = ' '
def posica_num(tup):
    num = tup[0]*3 + tup[1] + 1
    return num

def num_posica(num):
    linha = (num - 1) // 3
    coluna = (num - 1) % 3
    return (linha,coluna)
    
def printcerquilha(cerquilha):
    print("\n")
    print(" ",cerquilha[0][0], "|", cerquilha[0][1], "|", cerquilha[0][2])
    print("-" * 3, "+", "-" * 1, "+", "-" * 3)
    print(" ",cerquilha[1][0], "|", cerquilha[1][1], "|", cerquilha[1][2])
    print("-" * 3, "+", "-" * 1, "+", "-" * 3)
    print(" ",cerquilha[2][0], "|", cerquilha[2][1], "|", cerquilha[2][2])

    
def actions(state):
    posic = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == " ":
                posic.append((i, j))
    return posic

def result(state,action, player):
    cerquilhecopy = []
    for i in range(3):
        cerquilhecopy.append(state[i][:])
    cerquilhecopy[action[0]][action[1]] = player
    return cerquilhecopy

def terminal(state):
    vaz = 0
    for i in range(3):
        if state[i].count('X') == 3:
            return 'X'
        elif state[i].count('O') == 3:
            return 'O'
        vaz = vaz + state[i].count(' ')
    if state[0][0] == state[1][1] and state[1][1] == state[2][2] and state[2][2] != " ":
        return state[0][0]
    if state[0][2] == state[1][1] and state[2][0] == state[1][1] and state[2][0] != " ":
        return state[0][2]
    if vaz == 0:
        return "Empate"
    return False

def utility(state):
    term = terminal(state)
    if term:
        if term == 'X':
            return 1
        elif term == 'O':
            return -1
        elif term == 'Empate':
            return 0
    return False    
    

