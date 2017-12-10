def read_input(filename='day4.in'):
    with open(filename, 'r')  as file:
        lines = file.readlines()
        return lines


def valid_passphrase(words):
    wordset = set()
    for word in words:
        if word in wordset:
            return False
        wordset.add(word)
    return True


if __name__ == '__main__':
    count = 0
    for line in read_input():
        words = line.split()
        count += 1 if valid_passphrase(words) else 0
    print(count)