def convert(s):
    length = len(str(s))
    ans = int(0)
    for i in range(length):
        ans = int(ans)*2 + int(s[i])
    return int(ans)
def gcd(n,m):
    if int(m)==0:
        return n
    else:
        return gcd(int(m),int(n)%int(m))
test = int(input())
t = int(0)
while test!=0:
    test -=1
    t += 1
    s1 = str(input())
    s2 = str(input())
    n = convert(str(s1))
    m = convert(s2)
    if gcd(n,m)>1:
        print("Pair #{}: All you need is love!".format(int(t)))
    else:
        print("Pair #{}: Love is not all you need!".format(int(t)))