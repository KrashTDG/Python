# if a word starts with vowel, yay gets added to end of it
# if the world starts with consonant, the first letter moves to the end and ay gets added after it. also first letter is capitalized
line = 'My name is AL SWEIGART and I am 4,000 years old.'
vowel = ['a','e','i','o','u']

line = line.split()
for index, word in enumerate(line):
    if word[0].lower() in vowel:
        line[index] = word + 'yay'
    elif word[0].isalpha():
        line[index] = word[1].upper() + word[2:] + word[0] + 'ay'
        
line = ' '.join(line)
        
print(line)

# incomplete. old.yay, only first letter of the sentence should be capital not the rest and if entire word is Uppercase
# then yay or ay should also be uppercase