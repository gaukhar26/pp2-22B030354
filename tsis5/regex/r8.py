import re
text = "FvjuvVuvubBhgu"
print(re.findall('[A-Z][^A-Z]*', text))