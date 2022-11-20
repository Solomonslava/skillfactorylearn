def input_sequence(lst, number):
    if all(map(lambda x: x.isdigit(), lst.split())) and number.isdigit():
        return list(map(int, lst.split())), int(number)
    else:
        print('Вы ввели неверные данные, попробуйте еще раз!')
        return input_sequence()

def my_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = my_sort(L[:middle])
        right = my_sort(L[middle:])
        return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

def binary_search(array, element, left, right):
    if left > right:
        return left-1
    middle = (right+left) // 2
    if array[middle] == element:
        return middle - 1
    elif element < array[middle]:
        return binary_search(array, element, left, middle-1)
    else:
        return binary_search(array, element, middle+1, right)

lst, number = input_sequence(input("Введите последовательность:    "), input("Введите число:    "))

lst = my_sort(lst)
ind = binary_search(lst, number, 0, len(lst) -1)
print(f"Номер позиции элемента: {ind}.\nЭлемент: {lst[ind]}.\nСледующий элемент: {lst[ind+1]}")
