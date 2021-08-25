import random

def print_dice():
    y = True
    while y:
        n = random.randint(1,6)
        if n == 1:
            print('---------')
            print('|       |')
            print('|   O   |')
            print('|       |')
            print('---------')
            a = input('please enter "y" or  "n":  ')
            if a == "y":
                y = True
            else:
                y = False
        elif n == 2:
            print('---------')
            print('|O      |')
            print('|       |')
            print('|      O|')
            print('---------')
            a = input('please enter "y" or  "n":  ')
            if a == "y":
                y = True
            else:
                y = False
        elif n == 3:
            print('---------')
            print('|O      |')
            print('|   O   |')
            print('|      O|')
            print('---------')
            a = input('please enter "y" or  "n":  ')
            if a == "y":
                y = True
            else:
                y = False
        elif n == 4:
            print('---------')
            print('|O     O|')
            print('|       |')
            print('|O     O|')
            print('---------')
            a = input('please enter "y" or  "n":  ')
            if a == "y":
                y = True
            else:
                y = False
        elif n == 5:
            print('---------')
            print('|O     O|')
            print('|   O   |')
            print('|O     O|')
            print('---------')
            a = input('please enter "y" or  "n":  ')
            if a == "y":
                y = True
            else:
                y = False
        elif n == 6:
            print('---------')
            print('|O     O|')
            print('|O     O|')
            print('|O     O|')
            print('---------')

print_dice()