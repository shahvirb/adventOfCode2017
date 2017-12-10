def read_input(filename='day5.in'):
    with open(filename, 'r')  as file:
        lines = file.readlines()
        return lines


if __name__ == '__main__':
    def solve(calc_jmp):
        lines = read_input()
        instructions = [int(inst.strip()) for inst in lines]
        iptr = 0
        steps = 0
        try:
            while True:
                #print(iptr, instructions, steps)
                jmp = instructions[iptr]
                instructions[iptr] += calc_jmp(jmp)
                iptr += jmp
                steps += 1
        except IndexError:
            pass
        print(steps)
    
    solve(lambda x: 1)
    solve(lambda x: -1 if x >= 3 else 1)
    