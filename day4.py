def read_input(filename='day4.in'):
    with open(filename, 'r')  as file:
        lines = file.readlines()
        return lines


def valid_passphrase(words, process):
    wordset = set()
    for word in words:
        pword = process(word)
        if pword in wordset:
            return False
        wordset.add(pword)
    return True

if __name__ == '__main__':
    count1 = 0
    count2 = 0
    for line in read_input():
        words = line.split()
        count1 += 1 if valid_passphrase(words, lambda x: x) else 0
        count2 += 1 if valid_passphrase(words, lambda x: ''.join(sorted(x))) else 0
    print(count1, count2)