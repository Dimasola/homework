"""
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""

from itertools import count, cycle

#namber = [i for i in count(3) if i < 10] поясните почему такая запись не работает ?

def gen_count(arg1, arg2):
    namber = []
    for i in count(arg1):
        if i > arg2:
            break
        else:
            namber.append(i)
    return namber


def gen_cycle(arg1, arg2):
    namber2 = []
    el=0
    for i in cycle(arg1):
        if el >= arg2:
            break
        else:
            el+=1
            namber2.append(i)
    return namber2

g = gen_count(3, 10)
print(g)
print(gen_cycle('yes', 17))



