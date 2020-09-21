"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

with open('Test\DZ1.txt', 'w') as DZ1:
    user_data = 'данные что вы вводите'
    while True:
        user_data = input('введите данные')
        if user_data == '':
            break
        DZ1.write(user_data + '\n')
"""
Поясните почему не сработала такая запись 
with open('Test\DZ1.txt', 'w') as DZ1:
    user_data = 'данные что вы вводите'
    while user_data == '':
        user_data = input('введите данные')
        DZ1.write(user_data + '\n')
"""
