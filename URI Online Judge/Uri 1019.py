a = int(input())
hour   = a/3600
minute = (a%3600)/60
second = (a%3600)%60
print("%d:%d:%d" % (hour,minute,second))
