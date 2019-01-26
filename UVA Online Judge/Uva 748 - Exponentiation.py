while True:
    try:
        line = input().strip().split()
        index = line[0].find('.')
        d = int(5-index)*int(line[1])
        num = int(line[0].replace('.',''))
        num = str(pow(num,int(line[1])))
        left = num[:-1*int(d)]
        right = num[-1 * int(d):]
        print ('%s.%s' % (left, right.strip('0')))
    except EOFError:
        break
