with open('words.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip('\n')
        if line == line[::-1]:
            print(line)
