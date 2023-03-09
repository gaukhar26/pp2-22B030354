import re
my_string = input('enter a string ')
p = re.compile('a.*?b$')
s = p.findall(my_string)
if s:
    print('it\'s a match')
else:
    print('no match found')
