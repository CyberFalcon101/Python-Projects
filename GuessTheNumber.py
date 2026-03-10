# Copyright CyberFalcon101. Forks are allowed as long as the author is credited.
global guess
import random
print('Welcome to Guess the Number!')
print("There are 4 modes you can choose from: ")
print("1. Easy Mode: A number between 1-15.")
print("2. Medium Mode: A number between 1-30.")
print("3. Hard Mode: A number between 1-50.")
print("4. Customised Mode: A number between two values of your choice.")
def fun():
    global easy
    global medium
    global hard
    global custom
    ask = input('Easy, Medium, Hard or Customised mode (e/m/h/c)? ').lower()
    if ask == 'e':
        easy = True
        medium = False
        hard = False
        custom = False
        def fun2():
            global guess
            global n
            global clue
            var = input('Yes or No: Do you want clues (y/n)? ').lower()
            if var == 'y':
                clue = True
                n = random.randint(1,15)
                g=0
                guess=0
                while(g!=n):
                    try:
                        g=int(input('Guess the number: '))
                        guess = guess + 1
                        if g>n:
                            print('Too big.')
                        elif g<n:
                            print('Too small.')
                    except ValueError:
                        print('Invalid input. Please enter integers only.')
                print('Correct!')
            elif var == 'n':
                clue = False
                n = random.randint(1,15)
                g = 0
                guess=0
                while(g!=n):
                    try:
                        g=int(input('Guess the number: '))
                        guess = guess + 1
                        if g>n:
                            print('Too big.')
                        elif g<n:
                            print('Too small.')
                    except ValueError:
                        print('Invalid input. Please enter integers only.')
                print('Correct!')
            else:
                print('Invalid input.')
                fun2()
        fun2()           
    elif ask == 'm':
        easy = False
        medium = True
        hard = False
        custom = False
        def fun2():
            global guess
            global n
            global clue
            var = input('Yes or No: Do you want clues (y/n)? ').lower()
            if var == 'y':
                clue = True
                n = random.randint(1,30)
                g=0
                guess= 0
                while(g!=n):
                    try:
                        g=int(input('Guess the number: '))
                        guess = guess + 1
                        if g>n:
                            print('Too big.')
                        elif g<n:
                            print('Too small.')
                    except ValueError:
                        print('Invalid input. Please enter integers only.')
                print('Correct!')
            elif var == 'n':
                clue = False
                n = random.randint(1,30)
                g=0
                guess=0
                while(g!=n):
                    try:
                        g=int(input('Guess the number: '))
                        guess = guess + 1
                        if g>n:
                            print('Too big.')
                        elif g<n:
                            print('Too small.')
                    except ValueError:
                        print('Invalid input. Please enter integers only.')
                print('Correct!')
            else:
                print('Invalid input.')
                fun2()
        fun2()
    elif ask == 'h':
        easy = False
        medium = False
        hard = True
        custom = False
        def fun2():
            global guess
            global n
            global clue
            var = input('Yes or No: Do you want clues (y/n)? ').lower()
            if var == 'y':
                clue = True
                n = random.randint(1,50)
                g=0
                guess=0
                while(g!=n):
                    try:
                        g=int(input('Guess the number: '))
                        guess = guess + 1
                        if g>n:
                            print('Too big.')
                        elif g<n:
                            print('Too small.')
                    except ValueError:
                        print('Invalid input. Please enter integers only.')
                print('Correct!')
            elif var == 'n':
                clue = False
                n = random.randint(1,50)
                g=0
                guess = 0
                while(g!=n):
                    try:
                        g=int(input('Guess the number: '))
                        guess = guess + 1
                        if g>n:
                            print('Too big.')
                        elif g<n:
                            print('Too small.')
                    except ValueError:
                        print('Invalid input. Please enter integers only.')
                print('Correct!')
            else:
                print('Invalid input.')
                fun2()
        fun2()
    elif ask == 'c':
        easy = False
        medium = False
        hard= False
        custom = True
        def fun2():
            global guess
            global n
            global clue
            global q
            global q2
            var = input('Yes or No: Do you want clues (y/n)? ').lower()
            if var == 'y':
                clue = True
                print('What do you want the beginning and end number to be (e.g. 1-20)? ')
                def newfun():
                    try:
                        global q
                        q = int(input('First number(e.g. 1): '))
                    except ValueError:
                        print('Invalid input. Please enter integers only.')
                        newfun()
                newfun()
                def newfun2():
                    try:
                        global q2
                        q2 = int(input('Second number(e.g. 20): '))
                    except ValueError:
                        print('Invalid input. Please enter integers only.')
                        newfun2()
                newfun2()
                n = random.randint(q,q2)
                g=0
                guess =0
                while(g!=n):
                    try:
                        g=int(input('Guess the number: '))
                        guess = guess + 1
                        if g>n:
                            print('Too big.')
                        elif g<n:
                            print('Too small.')
                    except ValueError:
                        print('Invalid input. Please enter integers only.')
                print('Correct!')
            elif var == 'n':
                clue = False
                print('What do you want the beginning and end number to be (e.g. 1-20)? ')
                def newfun():
                    try:
                        global q
                        q = int(input('First number (e.g. 1): '))
                    except ValueError:
                        print('Invalid input. Please enter integers only.')
                        newfun()
                newfun()
                def newfun2():
                    try:
                        global q2
                        q2 = int(input('Second number (e.g. 20): '))
                    except ValueError:
                        print('Invalid input. Please enter integers only.')
                        newfun2()
                newfun2()
                g=0
                guess=0
                n = random.randint(q,q2)
                while(g!=n):
                    try:
                        g=int(input('Guess the number: '))
                        guess = guess + 1
                        if g>n:
                            print('Too big.')
                        elif g<n:
                            print('Too small.')
                    except ValueError:
                        print('Invalid input. Please enter integers only.')
                print('Correct!')
            else:
                print('Invalid input.')
                fun2()
        fun2()
    else:
        print('Invalid input.')
        fun()
fun()
print("Hope you enjoyed this program!")
if easy == True and clue == True:
    print('It took you', guess, 'guess(es) to find the number',n,'while you were on Easy Mode with clues.')
elif easy == True and clue == False:
    print('It took you', guess, 'guess(es) to find the number',n,'while you were on Easy Mode without clues.')
elif medium == True and clue == True:
    print('It took you', guess, 'guess(es) to find the number',n,'while you were on Medium Mode with clues.')
elif medium == True and clue == False:
    print('It took you', guess, 'guess(es) to find the number',n,'while you were on Medium Mode without clues.')
elif hard == True and clue == True:
    print('It took you', guess, 'guess(es) to find the number',n,'while you were on Hard Mode with clues.')
elif hard == True and clue == False:
    print('It took you', guess, 'guess(es) to find the number',n,'while you were on Hard Mode without clues.')
elif custom == True and clue == True:
    print('It took you', guess, 'guess(es) to find the number',n,'while you were on Custom Mode with clues.')
elif custom == True and clue == False:
    print('It took you', guess, 'guess(es) to find the number',n,'while you were on Custom Mode without clues.')
