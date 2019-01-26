s = input()
print(len({s[i:]+s[:i] for i in range(len(s))}))



s = input()
n = len(s)
a = set()
for i in range(n):
    a.add(s[i:] + s[:i])
print(len(a))
