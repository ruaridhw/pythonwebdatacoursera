import re

# Open text document
fhand = open('actualdata.txt')
text = fhand.read()

# Return a list of all numbers found
listofnums = re.findall('[0-9]+',text)

# Iterate through the list totalming the numbers
total = 0
for num in listofnums:
    total = total + int(num)

print total

print sum([int(num) for num in re.findall('[0-9]+',open('actualdata.txt').read())])
