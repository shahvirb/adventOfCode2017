def read_input(filename='day5.in'):
    with open(filename, 'r')  as file:
        lines = file.readlines()
        return lines


def timeit(method):
    import time
    # https://gist.github.com/OcupeSnippets/cbedc9ac5f40bcc211fff22c9b5b12b5
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print('[TimeIt] func: "{}" run in {}s'.format(method.__name__, te - ts))
        return result
    return timed

@timeit
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


if __name__ == '__main__':
    import timeit
    solve(lambda x: 1)
    solve(lambda x: -1 if x >= 3 else 1)
    