import random

def play(user, computer):
    user = input("Elige piedra, 'r', papel, 'p', o tijera, 't'")
    computer = random.choice(['r', 'p', 't'])

    if user == computer:
        return 'Empate'
    
    elif is_win:
        return 'Ganaste'

    else:
        return 'Perdiste'

def is_win(player, opponent):
    if (player == 'r' and opponent == 'p') or (player == 'p' and opponent == 't') or (player == 't' and opponent == 'r'):
        return True
    else:
        return False