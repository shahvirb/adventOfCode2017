def read_input(filename='day5.in'):
    with open(filename, 'r')  as file:
        lines = file.readlines()
        return lines


if __name__ == '__main__':
    lines = read_input()
    instructions = [int(inst.strip()) for inst in lines]
    iptr = 0
    steps = 0
    try:
        while True:
            #print(iptr, instructions, steps)
            jmp = instructions[iptr]
            instructions[iptr] += 1
            iptr += jmp
            steps += 1
    except IndexError:
        pass
    print(steps)