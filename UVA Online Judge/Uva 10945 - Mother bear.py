while True:
    try:
        store = []
        s = str(input())
        length = len(s)
        for c in enumerate(s):
            if (ord(c)>=65 and ord(c)<=90) or (ord(c)>=97 and  ord(c)<=122):
                print(c)
        print(store)
    except EOFError:
        break
