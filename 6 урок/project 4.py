"""
Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
"""


class Car:
    speed = 0
    color = ''
    name = ''
    is_police = False

    def go_stop(self):
        if not self.speed:
            return print('машина стоит')
        print('машина едет')


    def turn(self,direction):
        print(f'машина повернула на{direction}')


    def show_speed(self):
        print(f'текущая скорость {self.speed}')


class TownCar(Car):
    color = 'черный'
    speed = 70
    name = 'Renault'
    def show_speed(self):
        if self.speed > 60:
            return print(f'Превышение скорости!!, допустимые граници 0-60, текущая скорость {self.speed}')
        print(f'текущая скорость {self.speed}')


class SportCar(Car):
    speed = 140
    color = 'красный'
    name = 'ламборджини'

class WorkCar(Car):
    speed = 55
    color = 'Черный'
    name = 'лада веста'
    def show_speed(self):
        if self.speed > 40:
            return print(f'Превышение скорости!!, допустимые граници 0-40, текущая скорость {self.speed}')
        print(f'текущая скорость {self.speed}')


class PoliceCar(Car):
    speed = 200
    color = 'черно-белый'
    name = 'porsche 911'
    is_police = True


city = TownCar()
work = WorkCar()
sport = SportCar()
police = PoliceCar()
print(city.is_police)
print(city.show_speed())
print(city.turn('лево'))
print(city.go_stop())



