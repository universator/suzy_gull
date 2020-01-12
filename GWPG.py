import random
from random import choice
UP_CASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOW_CASE = 'abcdefghijklmnopqrstuvwxyz'
SPEC_SYM= '@#$_&+()/*!?=^%{}[]№'
Password = ''
print('Guy Fawkes Password Generator')
Dash = 0
while True:
    Strength = int(input('Enter the number of characters: '))
    if Strength > 0:
        while len(Password) < Strength:
            Symbol = random.randint(0,3)
            if Dash == 4:
                Add = '-'
                Dash = 0
            elif Symbol == 0:
                Add = choice(LOW_CASE)
                Dash += 1
            elif Symbol == 1:
                Add = choice(UP_CASE)
                Dash += 1
            elif Symbol == 2:
                Add = str(random.randint(0,9))
                Dash += 1
            elif Symbol == 3:
                Add = choice(SPEC_SYM)
                Dash += 1
            Password = Password + Add
        print(Password)
        if len(Password) < 10:
            print('Passwords longer than 16 characters are recommended')
    else:
            print('Enter a number greater than zero')
    Password = ''
    Dash = 0