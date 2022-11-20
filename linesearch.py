def find(array, element):
    for i, a in enumerate(array):
        if a == element:
            return i
    return False