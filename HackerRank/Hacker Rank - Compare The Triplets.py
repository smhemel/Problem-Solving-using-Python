a = [int(x) for x in input().split(" ")]
b = [int(x) for x in input().split(" ")]
print(sum([1 for x in range(3) if a[x] > b[x]]), sum([1 for x in range(3) if a[x] < b[x]]))
