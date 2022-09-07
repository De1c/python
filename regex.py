import re


my_text = 'My string will follow something to provide me some knowledge, also with symbols'
print(re.findall(r"\w+", my_text))
