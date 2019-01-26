fruit = {"apple": "It's colour is red", "lemon": "It's colour is Green",
         "orange": "It's colour is Yellow", "jambul": "It's colour is Blue"}
# del fruit
# fruit.clear()
'''while True:
    key = str(input("Enter a Key: "))
    if key == "quit":
        break
    else:
        description = fruit.get(key, key + " is not in the Dictionary")
        print(description)'''

item_keys = list(fruit.keys())
item_keys.sort()
for i in item_keys:
    print(i + ' - ' + fruit[i])

print("=" * 40)
for val in fruit.values():
    print(val)
print("=" * 40)
for key in fruit:
    print(fruit[key])

t_fruit = tuple(fruit.items())
print(t_fruit)
for snak in t_fruit:
    item, description = snak
    print (item + " = " + description)
num = {"A": 1, "B": 2, "C": 3}
num.update(fruit)
print(num)
nice_and_nusty = fruit.copy()
nice_and_nusty.update(num)
print(nice_and_nusty)
