#List
'''n = int(input())
l = []
for i in range(2,n,2):
    l.append(i)
length = len(l)
for i in range(int(length)):
    print("Index = {} Value = {}".format(i,l[i]))

print("="*20)

l[0] = 100
l[1] = 200
for i in range(int(length)):
    print("Index = {} Value = {}".format(i,l[i]))
'''

#Truples

pack = "Hridoy Khan", "Habib Wahid" , "Tanjib", ([(1, "Bolna"),(2,"Tumi Hina"), (3,"Hemel Haowa")])
print(pack)
pack[3].append((4,"Valo lage na"))
print(pack)
Singer,Singer1,Singer2,Songs = pack
print(Singer)
print(Singer1)
print(Singer2)
print(Songs)
Songs.append((5, "Aral"))
for song in Songs:
    track , title = song
    print("\tTrack No {}: {}".format(track , title))