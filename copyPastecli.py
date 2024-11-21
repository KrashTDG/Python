# you need to pass argument when you run the file
import sys,y_cant_I_name_this_pyperclip

TEXT = {'Hamilton': 'I\'m not throwing away my shot',
        'Angelica' : 'He\'ll never be satisfied',
        'Eliza' : 'look around, look around. How lucky we are to be alive rn'}

if len(sys.argv) > 2:
    print('Too many arguments given')
    print(len(sys.argv))
    sys.exit()

name = sys.argv[1]
if name in TEXT:
    y_cant_I_name_this_pyperclip.copy(TEXT[name])
    print(f'\'{y_cant_I_name_this_pyperclip.paste()}\' is copied')
else:
    print('The name is wrong')