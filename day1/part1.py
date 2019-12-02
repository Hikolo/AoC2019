from sys import argv
from math import floor

_script, fileName = argv

input = open(fileName)

fuel = 0

for weight in input:
    fuel += ((floor((int(weight) / 3))) - 2)

print(fuel)
