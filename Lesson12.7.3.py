per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму депозита:    '))
deposit = [round(i/100*money) for i in per_cent.values()]
print(deposit)
print(f'Максимальная сумма, которую вы можете заработать - {max(deposit)}')