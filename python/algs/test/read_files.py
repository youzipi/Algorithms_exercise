with open("./tinyUF.txt", 'r') as f:
    print(f.readline())
    # data = f.readlines()
    c = 0
    for line in f:
        # words = line.split()
        # print(words)
        c += 1
        print(c)
        print(line.split())
        # print(line[0])
        # print(line[1])
