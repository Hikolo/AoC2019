from math import floor
input = open('input')

fuel = 0

def calcFuel(mass):
    return(floor(mass / 3) - 2)
def addFuel(mass):
    if calcFuel(mass) <= 0:
        return 0
    else:
        return calcFuel(mass)


for mass in input:
    extraFuel = calcFuel(int(mass))
    while extraFuel > 0:
        fuel += extraFuel
        print(f"Extra fuel to add: {extraFuel}")
        extraFuel = calcFuel(int(extraFuel))
    print(f"Fuel after adding for fuel: {fuel}")
print(f"Total fuel: {fuel}")
    
