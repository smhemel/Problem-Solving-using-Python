import re
for _ in range(int(input())):
    s = str(input()).strip()
    for _ in range(int(input())):
        if re.search(str(input()).strip(), s):
            print ("y")
        else:
            print ("n")
