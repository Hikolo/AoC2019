from sys import argv
script, fileName = argv
input = open(fileName)
inputlist = input.read().split(',')
print(inputlist)
intlist = list(map(int, inputlist))
intlist[1] = 12
intlist[2] = 2
PC = 0
while PC <= len(intlist):
    OP = intlist[PC]
    if OP == 99:
        break
    A, B, C = intlist[PC + 1: PC + 4]
    print(f"A={A}, B={B}, C={C}")
    if OP == 1:
        Cin = intlist[A] + intlist[B]
    elif OP == 2:
        Cin = intlist[A] * intlist[B]
    else:
        print("Error!")
        break
    intlist[C] = Cin
    print(intlist)
    PC += 4
print(intlist[0])
        

        
