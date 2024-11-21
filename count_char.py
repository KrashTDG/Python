import pprint

he_lied = 'But are you surprised, darling you lied. well what\'s what on your mind, darling you lied.'
count = {}

for character in he_lied:
    count.setdefault(character,0)
    count[character] = count[character] + 1

pprint.pprint(count) 
