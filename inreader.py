def read_input(filename):
    with open(filename, 'r')  as file:
        contents = file.readlines()
        return contents[0].strip()
        