
def intcode(Noun, Verb):
    input = list(map(int, open('input').read().split(',')))
    input[1] = Noun
    input[2] = Verb
    PC = 0
    while PC <= len(input):
        OP = input[PC]
        if OP == 99:
            break
        A, B, C = input[PC + 1: PC + 4]
        if OP == 1:
            Cin = input[A] + input[B]
        elif OP == 2:
            Cin = input[A] * input[B]
        else:
            print("Error!")
            break
        input[C] = Cin
        PC += 4
    return input[0]

while True:
    for Noun in range(100):
        for Verb in range(100):
            Output = intcode(Noun, Verb)
            if Output == 19690720:
                print(100*Noun + Verb)
    break
