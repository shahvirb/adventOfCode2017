import inreader

def balance(blocks):
    holding = max(blocks)
    ind = blocks.index(holding)
    #print(holding, ind)
    rebalance = list(blocks)
    rebalance[ind] = 0
    for x in range(holding):
        ind = (ind + 1) % len(blocks)
        rebalance[ind] += 1
    #print(rebalance)
    return rebalance

# if __name__ == '__main__':
#     line = inreader.read_input('day6.in')
#     blocks = [int(l) for l in line.split()]
#     configs = [blocks]
#     cnt = 0
#     while True:
#         blocks = balance(blocks)
#         cnt += 1
#         if blocks in configs:
#             #print(configs)
#             break
#         configs.append(blocks)
#     print(cnt)
#     

if __name__ == '__main__':
    line = inreader.read_input('day6.in')
    blocks = [int(l) for l in line.split()]
    configs = [blocks]
    cnt = 0
    while True:
        blocks = balance(blo cks)
        cnt += 1
        if blocks in configs:
            prevIdx = configs.index(blocks)
            print(cnt)
            print(cnt - prevIdx)
            break
        configs.append(blocks)
    print(cnt)