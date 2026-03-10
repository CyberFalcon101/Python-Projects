#COPYRIGHT CyberFalcon101. Forks are allowed as long as the author is credited. 
print('Welcome to Calculator (Can Perform 7 Operations)')
print("NOTE: Operations that produce a result higher than 100000 digits may either freeze the program or output an error message. This typically happens when dealing with exponents.")
print("Also keep in mind that operations involving floating point numbers cannot work.")
def stuff():
    ask = input ('Add, Subtract, Multiply, Divide, or Further Options (a,s,m,d,f)? ').lower()
    if ask == 'a':
        Number1 = int(input('Type in the first number: '))
        Number2 = int(input('Type in the second number: '))
        add = str(Number1 + Number2)
        print ('The answer is: ' + add)
        re = input('Again (yes/no)? ').lower()
        if re == 'yes':
            stuff()
        elif re == 'no':
            print('Okay! I hope you enjoyed this program!')
    elif ask == 's':
        Number1 = int(input('Type in the first number: '))
        Number2 = int(input('Type in the second number: '))
        sub = str(Number1 - Number2)
        print ('The answer is: ' + sub)
        re = input('Again (yes/no)? ').lower()
        if re == 'yes':
            stuff()
        elif re == 'no':
            print('Okay! I hope you enjoyed this program!')
    elif ask == 'm':
        Number1 = int(input('Type in the first number: '))
        Number2 = int(input('Type in the second number: '))
        mul = str(Number1 * Number2)
        print ('The answer is: ' + mul)
        re = input('Again (yes/no)? ').lower()
        if re == 'yes':
            stuff()
        elif re == 'no':
            print('Okay! I hope you enjoyed this program!')
    elif ask == 'd':
        Number1 = int(input('Type in the first number: '))
        Number2 = int(input('Type in the second number: '))
        div = str(Number1 / Number2)
        print ('The answer is: ' + div)
        re = input('Again (yes/no)? ').lower()
        if re == 'yes':
            stuff()  
        elif re == 'no':
            print('Okay! I hope you enjoyed this program!')
    if ask == 'f':
        ask2 = input('Further options: Modulo, Floor Divison, Exponent (m,f,e)? ')
        if ask2 == 'm':
            Number1 = int(input('Type in the first number: '))
            Number2 = int(input('Type in the second number: '))
            mod = str(Number1 % Number2)
            print ('The answer is: ' + mod)
            re = input('Again (yes/no)? ').lower()
            if re == 'yes':
                stuff()
            elif re == 'no':
                print('Okay! I hope you enjoyed this program!')
        elif ask2 == 'f':
            Number1 = int(input('Type in the first number: '))
            Number2 = int(input('Type in the second number: '))
            flo = str(Number1 // Number2)
            print ('The answer is: ' + flo)
            re = input('Again (yes/no)? ').lower()
            if re == 'yes':
                stuff()
            elif re == 'no':
                print('Okay! I hope you enjoyed this program!')
        elif ask2 == 'e':
            Number1 = int(input('Type in the first number: '))
            Number2 = int(input('Type in the second number: '))
            exp = str(Number1 ** Number2)
            print ('The answer is: ' + exp)
            re = input('Again (yes/no)? ').lower()
            if re == 'yes':
                stuff()
            elif re == 'no':
                print('Okay! I hope you enjoyed this program!')           
stuff()
