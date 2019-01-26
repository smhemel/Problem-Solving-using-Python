animals = set(["lion","cow","cat","dog","snake","monkey"])
animals.add("horse")
print(animals)
even = set(range(0,40,2))
print(even)
print(sorted(even))
squares_tuple = (4,8,9,16,36)
square = set(squares_tuple)
print(square)
print(even.union(square))
print(even.intersection(square))
print(square & even)
print("even minus square")
print(sorted(even.difference(square)))
print(sorted(even.symmetric_difference(square)))
square.discard(9)
square.remove(16)
print(square)
try:
    square.remove(16)
except KeyError:
    print("This item is not in the set")
square.add(16)
if square.issubset(even):
    print("Square is a subset of even")
if even.issuperset(square):
    print("even is a superset of square")
even_t = frozenset(range(0,40,2))
#frozenset is not add any item
simpletext = "My name is Hemel. My subject is Computer engineering"
vowels = frozenset("aeiou")
dif = set(simpletext).difference(vowels)
print(dif)
