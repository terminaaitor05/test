import random

def play():
    user = input("Elige piedra, 'r', papel, 'p', o tijera, 't': ")
    computer = random.choice(['r', 'p', 't'])

    if user == computer:
        print('Empate')
    
    elif is_win(user, computer):
        print('Ganaste')

    else:
        print('Perdiste')

def is_win(user, computer):
    if (user == 'r' and computer == 'p') or (user == 'p' and computer == 't') or (user == 't' and computer == 'r'):
        return True
