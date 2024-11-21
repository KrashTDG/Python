import re 
regex = re.compile(r'[^aeiouAEIOU]+')
num = regex.findall('Let\'s pretend I\'m still Pekora')
print(num)
