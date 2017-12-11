import re

def read_input(filename='day7.in'):
    with open(filename, 'r')  as file:
        lines = file.readlines()
        return lines

roots = []

class Program():
    regex = "(\w+) \((\d+)\)(\s+->\s+)?(.*)"
    def __init__(self, name, weight, childNames):
        self.name = name
        self.weight = weight
        self.missingChildren = childNames
        self.children = []
        for childName in childNames:
            for root in roots:
                if childName == root.name:
                    self.children.append(root)
                    roots.remove(root)
                    break
        for child in self.children:
            self.missingChildren.remove(child.name)
    
def parse_program(line):
    match = re.search(Program.regex, line)
    name = match.group(1)
    weight =  int(match.group(2))
    childNames = []
    if match.group(3):
        childNames = [name.strip() for name in match.group(4).split(",")]
    return Program(name, weight, childNames)
    
def find_parent(prog, root):
    for name in root.missingChildren:
        if prog.name == name:
            root.children.append(prog)
            root.missingChildren.remove(prog.name)
            return True
    for child in root.children:
        if find_parent(prog, child):
            return True
    return False

def add_program(line):
    prog = parse_program(line)
    for root in roots:
        if find_parent(prog, root):
            break
    else:
        roots.append(prog)
        
if __name__ == '__main__':
    for line in read_input():
        add_program(line)
    print(roots[0].name)