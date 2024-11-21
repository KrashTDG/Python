import sys

def collatz(number):
    infinite = True
    while(infinite):
        
        if number < 0 or number == 0:
             print('input number again')
             number = int(input())
             continue
        
        if(number == 1):
            sys.exit()
        elif number % 2 == 0:
            number = number // 2
            print(number)
        
        elif number % 2 == 1:
            number = 3 * number + 1
            print(number)
num = int(input('Input Number: '))
collatz(num)