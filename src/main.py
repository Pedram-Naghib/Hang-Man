from random import choice

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def cyan(letter):
    return f"{bcolors.OKCYAN}{letter}{bcolors.ENDC}"

def red(letter):
    return f"{bcolors.FAIL}{letter}{bcolors.ENDC}"

def warn(wordd):
    return f"{bcolors.WARNING}{wordd}{bcolors.ENDC}"

def check(letter):
    ind = 0
    inds = []
    for i in letters:
        if i == letter:
            inds.append(ind)
        ind +=1
    return inds

with open('words.txt', 'r') as f:
    words = f.readlines()

word = choice(words).rstrip('\n').lower()
correct, guesses = len(word), 0
mistakes = 5
letters = [i for i in word]

place_holder = ['_ ' for _ in range(correct)]
print(*place_holder, warn(f'{mistakes} mistakes left.'))

invalids, valids = '', ''

while mistakes + 1 != 0 and correct != 0:
    letter = input('\n>> ')
    valid = check(letter.lower())
    if valid:
        for i in valid:
            if letter in valids:
                print("\033[94mYou've already tried this letter!!\033[0m")
            place_holder[i] = f'{cyan(letter) }'
            correct -= 1
            print(correct)
        valids += letter
        print(*place_holder, warn(f'{mistakes} mistakes left. {red(invalids)}'))
    else:
        if letter not in invalids:
            invalids += f'{letter} '
            mistakes -= 1
        if mistakes >= 0:
            print(*place_holder, warn(f'{mistakes} mistakes left. {red(invalids)}'))
        else:
            break
    guesses += 1

if correct == 0:
    print(f'Congratulation you have won in {guesses} guesses!')
else:
    print('\033[95m\nSorry you\'ve lost! word was --> \033[0m', end='')
    print(red(word))
    
