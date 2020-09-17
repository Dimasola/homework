"""
 Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
 Определить, кто из сотрудников имеет оклад менее 20 тыс.,
 вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
"""
with open('Test\DZ3.txt', 'r') as DZ3:
    dataDZ3 = DZ3.readlines()
    g = ''.join(dataDZ3)
    dataDZ3 = g.split()
    print(dataDZ3)
    salary = []
    keyses = []
    count = 1
    count2 = 0
    r_len = len(dataDZ3) - 1
    while count <= r_len:
        salary.append(int(dataDZ3[count]))
        count += 2
        keyses.append(dataDZ3[count2])
        count2 += 2
    dataDZ3_d = dict(zip(keyses, salary))
    print(dataDZ3_d)
    salary_sum = 0
    for el in dataDZ3_d:
        if dataDZ3_d.get(el) < 20:
            print(f'Сотрудник с окладом меньше 20 тысяч {el}')
        salary_sum = (salary_sum + dataDZ3_d.get(el))
    salary_sum /= len(keyses)
    print('Средний доход всех сотрудников', salary_sum)



