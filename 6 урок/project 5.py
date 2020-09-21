"""
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""
from time import sleep


class Stationery:
    title = ''

    def draw(self):
        print('запускаем отриссовку')


class Pen(Stationery):
    title = 'ручка'

    def draw(self):
        print('запускаем отриссовку')
        sleep(2)
        print('текст написан')


class Pencil(Stationery):
    title = 'карандаш'

    def draw(self):
        print('запускаем отриссовку')
        sleep(2)
        print('чертеж сделан')


class Handle(Stationery):
    title = 'маркер'

    def draw(self):
        print('запускаем отриссовку')
        sleep(2)
        print('нужные слова выделены')


res1 = Pen()
res2 = Pencil()
res3 = Handle()

print(res1.draw())
print(res2.draw())
print(res3.draw())
