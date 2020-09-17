"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
with open('Test\данные.txt', 'r') as Data_DZ4, open('Test\DZ4.txt', 'w') as DZ4:
    line = Data_DZ4.readlines()
    line = ''.join(line)
    line = str.split(line)
    print(line)
    for el in line:
        if el == 'One':
            line.insert(line.index(el), 'Один')
            line.remove(el)
        if el == 'Two':
            line.insert(line.index(el), 'Два')
            line.remove(el)
        if el == 'Three':
            line.insert(line.index(el), 'Три')
            line.remove(el)
        if el == 'Four':
            line.insert(line.index(el), 'Четыре')
            line.remove(el)
    for el in line:
        DZ4.write(''.join(el)+ ' ')
