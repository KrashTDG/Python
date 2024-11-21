# it takes however many lines you have copied and put bullet point before them
import pyperclip

text = pyperclip.paste()
lines = text.split('\n')

for i in range(len(lines)):
    lines[i] = (f'* {lines[i]}')

text = '\n'.join(lines)
pyperclip.copy(text)

