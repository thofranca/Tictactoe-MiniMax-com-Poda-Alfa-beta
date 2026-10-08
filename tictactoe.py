cerquilha = [
    ['X', 'O', 'X'],
    ['O', 'X', 'O'],
    ['O', 'X', 'O']
]

print(" ",cerquilha[0][0], "|", cerquilha[0][1], "|", cerquilha[0][2])
print("-" * 3, "+", "-" * 1, "+", "-" * 3)
print(" ",cerquilha[1][0], "|", cerquilha[1][1], "|", cerquilha[1][2])
print("-" * 3, "+", "-" * 1, "+", "-" * 3)
print(" ",cerquilha[2][0], "|", cerquilha[2][1], "|", cerquilha[2][2])

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
    if terminal(state) == 'X':
        return 1
    elif terminal(state) == 'O':
        return -1
    elif terminal(state) == 'Empate':
        return 0

print(terminal(cerquilha))
