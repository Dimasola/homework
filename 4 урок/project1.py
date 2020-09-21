"""
 Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv
script_name, production, rate, premium = argv

production = int(production)
rate = int(rate)
premium = int(premium)


def calculation_of_salary(*, arg=production, arg1=rate, arg2=premium):
    salary = (arg * arg1) + arg2
    return salary


print('выроботка в часах', production)
print('ставка в час', rate)
print('премия', premium)
print('ваша зарплата', calculation_of_salary(arg=production, arg1=rate, arg2=premium))

# python project1.py 300 150 8000