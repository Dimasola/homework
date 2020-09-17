"""
 Создать текстовый файл (не программно), сохранить в нем несколько строк,
  выполнить подсчет количества строк, количества слов в каждой строке.
"""
with open('Test\DZ1.txt', 'r') as DZ1:
    s = DZ1.readlines()
    quantity_str = len(s)
    for i, el in enumerate(s):
        quantity_words = len((el.split()))
        print(f'в строке {i} {quantity_words} слов')
    print("Всего строк", quantity_str)