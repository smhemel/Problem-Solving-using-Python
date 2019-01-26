d, s = 0, input()
for i in s:
    d += i.isupper()
if d > len(s) - d:
    print(s.upper())
else:
    print(s.lower())
