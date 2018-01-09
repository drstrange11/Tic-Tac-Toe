from __future__ import print_function
import random

flag=0
def print_board(l):
    for i in range(1,10):
        print(l[i], end='\t')
        if i % 3 == 0:
            print('\n')

def check(p,q):
    if (p=='x'and q=='o') or (p=='o' and q=='x'):
        global flag
        random_choice = random.choice([0, 1])
        if random_choice == 0:
            print('Player 1 starts the game')
        else:
            print('Player 2 starts the game')
            flag+=1
        return 1
    else:
        return 0

print('Welcome players!\nWhat do you want to do?')
a=True
while a:
    print('\n\n1.Play\n2.Exit')
    o1=int(input())
    if o1==1:

        l=[]
        for i in range(0,10):
            l.append('_')
        print('Choose who is Player 1 and Player 2 among yourselves and select what you are going to use (X/O)\n')
        print('The game randomly chooses who is going to start first! :P\n')
        a=raw_input('Player 1:\t')
        b=raw_input('Player 2:\t')
        a=a.lower()
        b=b.lower()
        while True:
            if(check(a,b)==1):
                break
            else:
                print("You have entered it wrong. Choose either X or O")
                a = raw_input('Player 1:\t')
                b = raw_input('Player 2:\t')
                a = a.lower()
                b = b.lower()

        for i in range(1,10):
            if flag==0:
                print('Player  1 - Enter the position you want to insert')
                pos = int(input())
                if(l[pos]=='X' or l[pos]=='O'):
                    print('The position already has an element')
                else:
                    l[pos]=a.upper()
                    flag=1
                    print_board(l)
            else:
                print('Player  2 - Enter the position you want to insert')
                pos = int(input())
                if (l[pos] == 'X' or l[pos] == 'O'):
                    print('The position already has an element')
                else:
                    l[pos]=b.upper()
                    flag=0
                    print_board(l)

            if l[1]=='X' and l[2]== 'X' and l[3]== 'X':
                if a=='x':
                    print('Player 1 wins!')
                else:
                    print('Player 2 wins!')
                break
            elif l[1]=='O' and l[2]=='O' and l[3]=='O':
                if a=='o':
                    print('Player 1 wins!')
                else:
                    print('Player 2 wins!')
                break
            elif l[1]=='X' and l[4]=='X' and l[7]=='X':
                if a=='x':
                    print('Player 1 wins!')
                else:
                    print('Player 2 wins!')
                break
            elif l[1]=='O' and l[4]=='O' and l[7]=='O':
                if a=='o':
                    print('Player 1 wins!')
                else:
                    print('Player 2 wins!')
                break
            elif l[7]=='X' and l[8]=='X' and l[9]=='X':
                if a=='x':
                    print('Player 1 wins!')
                else:
                    print('Player 2 wins!')
                break
            elif l[7]=='O' and l[8]=='O' and l[9]=='O':
                if a=='o':
                    print('Player 1 wins!')
                else:
                    print('Player 2 wins!')
                break
            elif l[3]=='X' and l[6]=='X' and l[9]=='X':
                if a=='x':
                    print('Player 1 wins!')
                else:
                    print('Player 2 wins!')
                break
            elif l[3]=='O' and l[6]=='O' and l[9]=='O':
                if a=='o':
                    print('Player 1 wins!')
                else:
                    print('Player 2 wins!')
                break
            elif l[1]=='X' and l[5]=='X' and l[9]=='X':
                if a=='x':
                    print('Player 1 wins!')
                else:
                    print('Player 2 wins!')
                break
            elif l[1]=='O' and l[5]=='O' and l[9]=='O':
                if a=='o':
                    print('Player 1 wins!')
                else:
                    print('Player 2 wins!')
                break
            elif l[3]=='X' and l[5]=='X' and l[7]=='X':
                if a=='x':
                    print('Player 1 wins!')
                else:
                    print('Player 2 wins!')
                break
            elif l[3]=='O' and l[5]=='O' and l[7]=='O':
                if a=='o':
                    print('Player 1 wins!')
                else:
                    print('Player 2 wins!')
                break

        print('\nGAME OVER!\nWhat do you want to do now?')

    else:
        break
