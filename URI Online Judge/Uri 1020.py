a = int(input())
year = a/365
month = (a%365)/30
day = ((a%365)%30)
print("%d ano(s)\n%d mes(es)\n%d dia(s)" %(year,month,day))
