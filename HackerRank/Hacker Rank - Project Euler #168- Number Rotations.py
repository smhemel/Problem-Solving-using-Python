num = int (input ())
high = 10 ** num
sum = 0
for i in range (11, high):
    istr = str (i)
    istr2 = istr [1:] + istr [0]
    i2 = int(istr2)
    if ((i2 % i) == 0):
        sum=(sum+i)%100000
        #sum = sum + i
print(sum)
