import random
import os

warriors = {1:'Rock', 2:'Paper', 3:'Scissors'}

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def main(p_choice):
    cpu_choice = warriors[random.randint(1, 3)]
    if cpu_choice == p_choice:
        print(f'\nIt`s a tie! You both choose {cpu_choice}')
    elif (cpu_choice == 'Rock' and p_choice == 'Paper') or (cpu_choice == 'Paper' and p_choice == 'Scissors') or (cpu_choice == 'Scissors' and p_choice == 'Rock'):
        print(f'\nYou won! The cpu picked {cpu_choice}!')
    elif (cpu_choice == 'Rock' and p_choice == 'Scissors') or (cpu_choice == 'Paper' and p_choice == 'Rock') or (cpu_choice == 'Scissors' and p_choice == 'Paper'):
        print(f'\nYou lose! The cpu picked {cpu_choice}!')
    else:
        cls()
        print('You picked an invalid number, try again.\n')
        return 0
    loop = str(input('Do you want to play again? (y/n): '))
    cls()
    return loop

while True:
    try:
        loop = main(warriors[int(input('Pick a warrior: \n1. Rock (Defense ++) (Bludgeon +++) \n2. Paper (Sharpness +++) (Swiftness +) \n3. Scissors (Cutting +++) (Resistance -)\n'))])
        if loop == 'n' or loop == 'N': break
    except ValueError:
        cls()
        print('Use only full numbers please!\n')