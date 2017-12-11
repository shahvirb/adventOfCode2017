def read_input(filename='day8.in'):
    with open(filename, 'r')  as file:
        lines = file.readlines()
        return lines


class Instruction:
    def __repr__(self):
        return ', '.join(str(x) for x in [self.modify, self.how, self.amount, self.lop, self.cond, self.rop])

def parse_line(string):
    import re
    REGEX = '(\w+) (inc|dec) (-?\d+) if (\w+) ([!=<>]+) (-?\d+)'
    matches = re.search(REGEX, string)
    ins = Instruction()
    ins.modify = matches.group(1)
    ins.how = matches.group(2)
    ins.amount = int(matches.group(3))
    ins.lop = matches.group(4)
    ins.cond = matches.group(5)
    ins.rop = int(matches.group(6))
    return ins


def eval(lop, cond, rop):
    import operator
    CONDITIONS = {'>':operator.gt,
                  '<':operator.lt,
                  '==':operator.eq,
                  '<=':operator.le,
                  '>=':operator.ge,
                  '!=':operator.ne}
    return CONDITIONS[cond](lop, rop)


def exec(how, amount):
    mult = 1 if how == 'inc' else -1
    return amount * mult


if __name__ == '__main__':
    registers = {}
    highest = 0
    for line in read_input():
        inst = parse_line(line)
        #print(inst)
        x = registers.setdefault(inst.lop, 0)
        if eval(x, inst.cond, inst.rop):
            registers.setdefault(inst.modify, 0)
            registers[inst.modify] += exec(inst.how, inst.amount)
        highest = max(max(registers.values()), highest)
        #print(registers)
    print(max(registers.values()))
    print(highest)
