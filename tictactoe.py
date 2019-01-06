from __future__ import print_function
import random

flag = 0


def print_board(l):
    for i in range(1, 10):
        print(l[i], end='\t')
        if i % 3 == 0:
            print('\n')


def check(p, q):
    if (p == 'x'and q == 'o') or (p == 'o' and q == 'x'):
        global flag
        random_choice = random.choice([0, 1])
        if random_choice == 0:
            print('Player 1 starts the game')
        else:
            print('Player 2 starts the game')
            flag += 1
        return 1
    else:
        return 0


print('Welcome players!\nWhat do you want to do?')
a = True
while a:
    print('\n\n1.Play\n2.Exit')
    o1 = int(input())
    if o1 == 1:

        l = []
        for i in range(0, 10):
            l.append('_')
        print('Choose who is Player 1 and Player 2 among yourselves and select what you are going to use (X/O)\n')
        print('The game randomly chooses who is going to start first! :P\n')
        a = raw_input('Player 1:\t')
        b = raw_input('Player 2:\t')
        a = a.lower()
        b = b.lower()
        while True:
            if(check(a, b) == 1):
                break
            else:
                print("You have entered it wrong. Choose either X or O")
                a = raw_input('Player 1:\t')
                b = raw_input('Player 2:\t')
                a = a.lower()
                b = b.lower()
        f1 = 0
        for i in range(1, 10):
            if flag == 0:
                print('Player  1 - Enter the position you want to insert')
                pos = int(input())
                if(l[pos] == 'X' or l[pos] == 'O'):
                    print('The position already has an element')
                else:
                    l[pos] = a.upper()
                    flag = 1
                    print_board(l)
            else:
                print('Player  2 - Enter the position you want to insert')
                pos = int(input())
                if (l[pos] == 'X' or l[pos] == 'O'):
                    print('The position already has an element')
                else:
                    l[pos] = b.upper()
                    flag = 0
                    print_board(l)

            if l[1] == l[2] == l[3] == 'X' or \
                l[4] == l[5] == l[6] == 'X' or \
                l[7] == l[8] == l[9] == 'X' or \
                l[1] == l[4] == l[7] == 'X' or \
                l[2] == l[5] == l[8] == 'X' or \
                l[3] == l[6] == l[9] == 'X' or \
                    l[1] == l[5] == l[9] == 'X' or \
                    l[3] == l[5] == l[7] == 'X':
                if a == 'x':
                    print('Player 1 wins!')
                else:
                    print('Player 2 wins!')
                break

            elif l[1] == l[2] == l[3] == 'O' or \
                l[4] == l[5] == l[6] == 'O' or \
                l[7] == l[8] == l[9] == 'O' or \
                l[1] == l[4] == l[7] == 'O' or \
                l[2] == l[5] == l[8] == 'O' or \
                l[3] == l[6] == l[9] == 'O' or \
                    l[1] == l[5] == l[9] == 'O' or \
                    l[3] == l[5] == l[7] == 'O':
                if a == 'o':
                    print('Player 1 wins!')
                else:
                    print('Player 2 wins!')
                break

            elif i == 9:
                for j in range(1, 10):
                    if l[j] != '_':
                        f1 += 1
                if f1 == 9:
                    print('DRAW!\n')

        print('\nGAME OVER!\nWhat do you want to do now?')

    else:
        break
