import re
my_string = input('enter a string ')
p = re.compile('a.*?b$')
camel_to_snake = p.sub(r"(\w)([A-Z])", r"\1_\2").lower()
    print(camel_to_snake)