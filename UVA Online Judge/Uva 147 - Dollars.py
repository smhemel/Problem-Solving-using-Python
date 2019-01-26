way = []
coin = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
way.append(int(1))
for i in range(11):
    for j in range(coin[int(i)], 30011):
        way[int(j)] = way[int(j)] + way[int(j)-coin[int(i)]]
while True:
    try:
        n = input()

    except EOFError:
        break