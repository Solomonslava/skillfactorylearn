array = [9, 3, 1, 4, 6, 5, 2, 8, 7]

for i in range(len(array)):
    for j in range(len(array)-i-1):
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]
    print(array)

print(array)