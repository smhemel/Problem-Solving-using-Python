str = str(input())
j = 0
s = 'heidi#'
for i in str:
    if i == s[j]:
        j += 1
print ('YES' if j == 5 else 'NO')