# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def summa(arg1, arg2, arg3):
    if arg1 >= arg2:
        a = arg1
    else:
        a = arg2
    if arg2 >= arg3:
        b = arg2
    else:
        b = arg3
    argSum = a + b
    return argSum


res = summa(4, 2, 1)
print(res)
