arr = [1, 2, 3, 4, 5, 6, 43, 23, 4, 1, 2, 4, 5, 3, 21, 3, 4, 5, 21, 3, 4, 5]
number = int(input('enter number to find'))
count = 0

for i in arr:
    if (number == i):
        count += 1
print(count)
