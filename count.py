def count(array, element):
    count = 0

    for i in array:
        if i == element:
            count += 1
    return count