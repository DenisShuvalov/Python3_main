from random import choice


class Car:
    """ Main car """
    direction = ["north", "northwest", "east", "southeast", "south", "southwest", "west", "northwest"]

    def _init_(self, n, c, s, p=False):
        self.name = n
        self.color = c
        self.speed = s
        self.is_police = p
        print(f'New car: {n} has a color: {c}.\nIs the car a police? {p}')

    def go(self):
        print(f'{self.name}: Car went.')

    def stop(self):
        print(f'{self.name}: Car stopped.')

    def turn(self):
        print(f'{self.name}: Car turned {choice(self.direction)}.')

    def show_speed(self):
        return f'{self.name}: Car speed: {self.speed}.'


class TownCar(Car):
    """ Town car """

    def show_speed(self):
        return f'{self.name}: Car speed: {self.speed}. Speeding!' if self.speed >= 60 else super().show_speed()


class WorkCar(Car):
    """Cargo track"""

    def show_speed(self):
        return f'{self.name}: Car speed: {self.speed}. Speeding!' if self.speed > 40 else super().show_speed()


class SportCar(Car):
    """ Sportcar """


class PoliceCar(Car):
    """ Police car """

    def __init__(self, n, c, s, p=True):
        super().__init__(n, c, s, p)


police_car = PoliceCar('Полицейская', 'белый', 80)
work_car = WorkCar('Грузовик', 'черный', 40)
sport_car = SportCar('Спортивная', 'красный', 100)
town_car = TownCar('Городской автомобиль', 'серый', 60)

car_list = [police_car, work_car, sport_car, town_car]

for i in car_list:
    i.go()
    print(i.show_speed())
    i.turn()
    i.stop()
    print()