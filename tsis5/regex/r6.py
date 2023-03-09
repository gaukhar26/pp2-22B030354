import re
text = 'Gvunds Vvndsl, PHP wndjka.'
print(re.sub("[ ,.]", ":", text))