#Пользователь вводит месяц в виде целого числа от 1 до 12.
#Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.


month = ['январь','февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
user_month = int(input('введите число месяца'))
if month[user_month-1] == (month[11]) or (month[0]) or (month[1]):
    print('введенный месяц', month[user_month-1], 'время года зима')

elif month[user_month-1] == (month[2]) or (month[3]) or (month[4]):
    print('введенный месяц', month[user_month-1], 'время года весна')

elif month[user_month-1] == (month[5]) or (month[4]) or (month[7]):
    print('введенный месяц', month[user_month-1], 'время года лето')

elif month[user_month-1] == (month[8]) or (month[9]) or (month[10]):
    print('введенный месяц', month[user_month-1], 'время года осень')



#  через dict

#my_dict = {1: "зима", 2: "зима", 3: "весна", 4: "весна", 5: "весна", 6: "лето", 7:  "лето", 8:  "лето", 9: "осень", 10: "осень", 11: "осень", 12: "зима" }
#user_month = int(input("введите число месяца"))
#print(my_dict.get(user_month))


