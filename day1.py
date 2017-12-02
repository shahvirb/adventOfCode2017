# http://adventofcode.com/2017/day/1

import inreader
import collections



if __name__ == '__main__':
    #input = inreader.read_input('day1.in')
    input = '1122'
    print(input)
    
    input = [int(i) for i in input]
    matches = []
    for ind, d in enumerate(input):
        match = d - 1
        print(d, match)
        count = 0
        for i in range(ind-1, ind-len(input), -1):
            if match == input[i]:
                count += 1
            else:
                break
        if count > 1:
            matches.append(match)
    
    print('Matches: {}'.format(matches))
    print('Answer: {}'.format(sum(matches)))