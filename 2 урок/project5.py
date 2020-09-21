#  Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
#  У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
#  то новый элемент с тем же значением должен разместиться после них.

my_list = [6, 4, 8, 2, 5, 9, 7, 3]
print(my_list)
user_number = int(input("введите число"))
if user_number in my_list:
    my_list.insert(my_list.index(user_number), user_number)
    print(my_list)
else:
    my_list.append(user_number)
    print(my_list)

