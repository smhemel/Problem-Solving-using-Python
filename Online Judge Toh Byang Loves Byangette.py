while True:
    try:
        n = str(input())
        if n == "Who loves Byang?":
            print("Byangette")
        else:
            print("Byang")
    except EOFError:
        break
