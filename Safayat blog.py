'''def goldbach():
  k = 4
  while True:
    ok = False     
    for p1  in range(k):
     for p2 in range(k):
      if(prime(p1) and prime(p2) and p1+p2==k):
        ok = True
    if not ok:
      exit()
    k += 2
x = goldbach(5)'''


def mysqrt(X):
    low=0.0
    high=X
    while high-low>.0001:
      mid=(low+high)/2
      print (low,high,mid,(mid*mid))
      if mid*mid>X:
        high = mid
      else:
        low = mid
    print("\n")
    print (mid,mid*mid)
    return mid
mysqrt(15)
