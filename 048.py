s = 0

for i in range(0, 500):
    if (i % 2 != 0) and (i % 3 == 0):
        s += i
print(s)
