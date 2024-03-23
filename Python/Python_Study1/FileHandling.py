import os
import shutil

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    file_path = 'D:\\Usuario\\Rpg Novo\\TxTs\\1d100damorte.txt'

    cls()
    if os.path.exists(file_path) and os.path.isfile('copy.txt') is False:
        shutil.copy(file_path, 'copy.txt')
        print('Copied into copy.txt')
    else:
        print('Generating new file...')
        with open(file_path, 'w+') as f:
            f.write(input('Type what do you want to write to the file:\n'))