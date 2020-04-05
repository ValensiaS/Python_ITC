fruits = ["monkey", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "apple":
        break

for x in range(2, 6, 1):
    print(x)
'''
2
3
4
5
'''
for x in range(6):
    print(x)

i = 0
test = True
while test:
    i += 1
    print(i)
    if i == 5:
        test = False