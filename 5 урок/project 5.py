"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
from functools import reduce

dz = open('Test\DZ5.txt', 'w')
dz.write('95 45 87 256 45 9 8 7 5')
dz.close()

with open('Test\DZ5.txt', 'r') as DZ5:
    user_namber = DZ5.readlines()
    user_namber = "".join(user_namber)
    user_namber = str.split(user_namber)
    res_namber = []
    for el in user_namber:
        r = int(el)
        res_namber.append(r)
    namber_sum = reduce(lambda x, y: x + y, res_namber)
    print(f'Сумма чисел ровна {namber_sum}')
