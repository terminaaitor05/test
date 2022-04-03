import random

def play():
    user = input("Elige piedra, 'r', papel, 'p', o tijera, 't'")
    computer = random.choice(['r', 'p', 't'])

    if user == computer:
        return 'Empate'
    
    if is_win(user, computer):
        return 'Ganaste'

    return 'Perdiste'

def is_win(user, computer):
    if (user == 'r' and computer == 'p') or (user == 'p' and computer == 't') or (user == 't' and computer == 'r'):
        return True

print(play())