
# Write a Python program to find the repeated items of a tuple.

m = (1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 2, 9, 3)
r = []

for item in m:
    if m.count(item) > 1 and item not in r:
        r.append(item)

print(r)

