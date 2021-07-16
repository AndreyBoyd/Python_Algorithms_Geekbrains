# Пользователь вводит данные о количестве предприятий, их наименования и прибыль
# за квартал для каждого. Программа должна определить среднюю прибыль и вывести наименования предприятий,
# чья прибыль выше среднего. Отдельно вывести наименования предприятий, чья прибыль ниже среднего


from collections import namedtuple

Q = 4
Company = namedtuple('Company', ['name', 'quarters', 'profit'])
all_comp = set()

num = int(input("Количество организаций: "))
total_profit = 0
for i in range(1, num + 1):
    profit = 0
    quarters = []
    name = input(f'Название организации {i}: ')

    for j in range(Q):
        quarters.append(int(input(f'Прибыль за {j + 1}-й квартал (введите целое число), тыс.руб: ')))
        profit += quarters[j]

    comp = Company(name=name, quarters=tuple(quarters), profit=profit)
    all_comp.add(comp)

avr = total_profit / num

print(f'Средняя прибыль: {avr}')

print(f'Имеют прибыль выше среднего:')
for comp in all_comp:
    if comp.profit > avr:
        print(f'{comp.name} прибыль {comp.profit}')

print(f'Имеют прибыль ниже среднего:')
for comp in all_comp:
    if comp.profit < avr:
        print(f'{comp.name} прибыль {comp.profit}')
