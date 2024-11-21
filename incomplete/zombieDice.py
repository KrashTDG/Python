import random,time,sys,os

def diceRoll():
   
    Dice = {'Red Dice' : ('footsteps', 'brains', 'shotgun', 'shotgun', 'shotgun', 'shotgun'),
             'Green Dice' : ('footsteps', 'brains', 'brains', 'brains', 'brains', 'shotgun'),
             'Yellow Dice' : ('footsteps', 'brains', 'brains', 'shotgun', 'shotgun', 'footsteps')        
    }
    result = {}
    for i in range(0,3):
        diceName, diceFace = random.choice(list(Dice.items()))
        faceName = random.choice(diceFace)
        print(f'{diceName} shows {faceName}')
        time.sleep(0.75)
        result.setdefault(faceName,0)
        result[faceName] += 1 
        
    return result

def addToRes(result, diceRoll):
    for items, count in diceRoll.items():
        result.setdefault(items,0)
        result[items] += count

def emptyRes(result):
    for items in result.keys():
        result[items] = 0
    return result


def BotA(): # Randomly decides after every turn whether to roll further or not
    print('Bot A'.center(20,'-')+'\nTurn 1:')
    result = diceRoll()
    print(f'{result}')
    count = 2
    while count <= 4:
        choice =  random.randint(0,1)
        if result.get('shotgun',0) < 3:
            if choice == 1:
                print(f'Turn {count}:')
                addToRes(result,diceRoll())
                print(f'{result}')
                count += 1
            else:
                print('Decided not to roll further')
                break
        else:
            print('Got 3 Shotguns')
            result = emptyRes(result)
            break
    if result.get('shotgun', 0) >= 3:
        print('Got 3 Shotguns')
        result = emptyRes(result)
    return result            


def BotB(): # stops rolling after it has rolled two shotguns
    print('\n'+'Bot B'.center(20,'-')+'\nTurn 1:')
    result = diceRoll()
    print(f'{result}')
    count = 2
    while count <= 4:
        if result.get('shotgun',0) < 3:
            if result.get('shotgun',0) < 2:
                print(f'Turn {count}:')
                addToRes(result,diceRoll())
                print(f'{result}')
                count += 1
            else:
                print('Decided not to roll further')
                break
        else:
            print("Got 3 Shotguns")
            result = emptyRes(result)
            break    
    if result.get('shotgun', 0) >= 3:
        print('Got 3 Shotguns')
        result = emptyRes(result)
    return result      
    
def BotC(): # initially decides it’ll roll the dice one to four times, but will stop early if it rolls two shotguns
    print('\n'+'Bot C'.center(20,'-')+'\nTurn 1:')
    result = diceRoll()
    print(f'{result}')
    choice = random.randint(0,3)
    count = 2
    for i in range(choice):
        if result.get('shotgun',0) < 3:
            if result.get('shotgun',0) < 2:
                    print(f'Turn {count}:')
                    addToRes(result,diceRoll())
                    print(f'{result}')
                    count += 1
            else:
                print('Decided not to roll further')
                break
        else:
            print("Got 3 Shotguns")
            result = emptyRes(result)
            break
    if result.get('shotgun', 0) >= 3:
        print('Got 3 Shotguns')
        result = emptyRes(result)
    return result           
      
            
def BotD(): # stops rolling after it has rolled more shotguns than brains
    print('\n'+'Bot D'.center(20,'-')+'\nTurn 1:')
    result = diceRoll()
    print(f'{result}')
    count = 2
    while count <= 4:
        if result.get('shotgun',0) < 3:
            if result.get('shotgun',0) <= result.get('brains',0):
                print(f'Turn {count}:')
                addToRes(result,diceRoll())
                print(f'{result}')
                count += 1
            else:
                print('Decided not to roll further')
                break
        else:
            print('Got 3 Shotguns')
            result = emptyRes(result)
            break
    if result.get('shotgun', 0) >= 3:
        print('Got 3 Shotguns')
        result = emptyRes(result)
    return result   
    

try:        
    def main():  
        resultA = BotA()
        resultB = BotB()
        resultC = BotC()
        resultD = BotD()
        time.sleep(.75)
        os.system('cls')
        print(f'Bot A: {resultA}\nBot B: {resultB}\nBot C: {resultC}\nBot D: {resultD}')
    main()
except KeyboardInterrupt:
    sys.exit()
        
    
