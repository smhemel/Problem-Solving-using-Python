def i_sqrt(n):
    i = int(n).bit_length() >> 1
    m = 1 << i
    while int(m)*int(m) > int(n):
        m >>= 1
        i -= 1
    for k in range(i-1, -1, -1):
        x = m | (1 << k)
        if int(x)*int(x) <= int(n):
            m = x
    return str(m)
test = int(input())
input()
for _ in range(test):
    while (1):
        n = input()
        if n!=" ":
            break;
    st = str(i_sqrt(n))
    print(st)
    print()
