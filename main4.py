class Car:
    def __init__(self, name, color, speed, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def car_on_go(self):
        return f'Машина {self.name} поехала'

    def car_on_stop(self):
        return f'\nМашина {self.name} прекратила движение'

    def turn(self, direction):
        return f'\nМашина {self.name} повернула {direction} '

    def show_speed(self):
        return f'Ваша скорость составляет {self.speed}'

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\n Вы превысили скорость! Ваша скорость составляет {self.speed} снизьте скорость до 60 км/ч'
        else: f"\n {self.speed} Скорость не превышена"


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\n Вы превысили скорость! Ваша скорость составляет {self.speed} снизьте скоро до 40 км/ч'
        else:
            f'\n {self.speed} Скорость не превышена'


class PoliceCar(Car):
    pass


towncar = TownCar('AudiA5', 'black', 79, False)
sportcar = SportCar('Ferrari', 'red', 250, False)
workcar = WorkCar('Gazele', 'white', 30, False)
policecar = PoliceCar('hyundai Solaric', 'blue and white', 100, True)
print('1:\n' + towncar.car_on_go(), towncar.show_speed(), towncar.turn('left'), towncar.turn('left'), towncar.turn('right'), towncar.car_on_stop())
print('2:\n' + sportcar.car_on_go(), sportcar.show_speed(), sportcar.car_on_stop())
print('3:\n' + workcar.car_on_go(), workcar.show_speed(), workcar.turn('right'), workcar.car_on_stop())
print('4:\n' + policecar.car_on_go(), policecar.show_speed(), policecar.turn('left'), policecar.turn('right'), policecar.car_on_stop())