import random
import os

warriors = ('Rock', 'Paper', 'Scissors')

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def main(p_choice):
    cls()
    cpu_choice = random.choice(warriors)
    
    print('Your Warrior: '+p_choice)
    print('Cpu`s Warrior: '+cpu_choice)
    
    if cpu_choice == p_choice:
        print(f'\nIt`s a tie!')
    elif (cpu_choice == 'Rock' and p_choice == 'Paper') or (cpu_choice == 'Paper' and p_choice == 'Scissors') or (cpu_choice == 'Scissors' and p_choice == 'Rock'):
        print(f'\nYou won! :)')
    elif (cpu_choice == 'Rock' and p_choice == 'Scissors') or (cpu_choice == 'Paper' and p_choice == 'Rock') or (cpu_choice == 'Scissors' and p_choice == 'Paper'):
        print(f'\nYou lose! :(')
    else:
        cls()
        print('You picked an invalid number, try again.\n')
        return 0
    loop = str(input('Do you want to play again? (y/n): '))
    cls()
    return loop

while True:
    try:
        loop = main(str(input('Pick a warrior: \nRock (Defense ++) (Bludgeon +++) \nPaper (Sharpness +++) (Swiftness +) \nScissors (Cutting +++) (Resistance -)\n')))
        if loop == 'n' or loop == 'N': break
    except ValueError:
        cls()
        print('Write the warrior`s name as shown please!\n')