MAX = 361527
#MAX = 13

def gen_spiral_commands(max=100):
    edge_len = 1
    for i in range(max):
        for j in range(edge_len):
            yield 'R'
        for j in range(edge_len):
            yield 'U'
        edge_len += 1
        for j in range(edge_len):
            yield 'L'
        for j in range(edge_len):
            yield 'D'
        edge_len += 1


class PositionMarker():
    def __init__(self, x=0, y=0):
        self.x = 0
        self.y = 0
        
    def move(self, cmd):
        move_map = {'R': (0, 1),
                    'U': (1, 0),
                    'L': (0, -1),
                    'D': (-1, 0)}
        dx, dy = move_map[cmd]
        self.x += dx
        self.y += dy


if __name__ == '__main__':
    p = PositionMarker()
    i = 1
    for cmd in gen_spiral_commands(1000000000):
        p.move(cmd)
        i += 1
        
        if i >= MAX:
            print(cmd, p.x, p.y, i)
            print('Answer = {}'.format(abs(p.x) + abs(p.y)))
            break
    
