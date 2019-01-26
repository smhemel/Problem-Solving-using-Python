while True:
    try:
        line = input().strip().split()
        if line[1] == '/':
            print(int(int(line[0])/int(line[2])))
        else:
            print(int(int(line[0])%int(line[2])))
    except:
        break
