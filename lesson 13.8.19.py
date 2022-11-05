amount = int(input('Количество билетов:   '))
list_of_age = [int(input(f'Какой возраст посетителя #{i} ?:   ')) for i in range(1, amount+1)]
total = 0

for i in list_of_age:
    if i < 18:
        continue
    elif 18 <= i < 25:
        total += 990
    else:
        total += 1390
if amount > 3:
    total *= 0.9

print('Общая сумма равна:', int(total))