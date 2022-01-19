# 1

from time import sleep


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        i = 0
        while i < 3:
            print(f'Светофор переключается \n '
                  f'{TrafficLight.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(3)
            i += 1


TrafficLight = TrafficLight()
TrafficLight.running()


# 2


class Road:
    _length = 0
    _width = 0

    def __init__(self, _length, _width, weight, thickness):
        self._length = _length
        self._width = _width
        self.weight = weight
        self.thickness = thickness

    def mass(self):
        l = self._length
        wi = self._width
        we = self.weight
        t = self.thickness
        total = l * wi * we * t / 1000
        return print(f"Масса асфальта\n {l} м * {wi} м * {we} кг * {t} см = ", total, "т.")


r = Road(20, 5000, 25, 5)
r.mass()


# 3

class Worker:
    # атрибуты класса
    name = "Екатерина"
    surname = "Шабалова"
    position = "Data scientist"
    profit = 50000
    bonus = 50000
    _income = {"Оклад": profit, "Премия": bonus}
    total_profit = 0


class Position(Worker):
    def get_full_name(self):
        return "{} \"{} {}\"".format(self.position, self.name, self.surname)

    def get_full_profit(self):
        self.total_profit = self.profit + self.bonus
        return ", доход с учётом премии: {}".format(self.total_profit)


w = Worker()
print(w.name)
print(w.surname)
print(w.position)
print(w.profit)

p = Position()
print(p.get_full_name() + str(p.get_full_profit()) + " " + str(w._income))


# 5

class Stationery:
    title = "\n<< Канцелярская принадлежность >>"

    def draw(self):
        print("Родительский метод класса Stationery")
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("\nРодительский метод класса Pen")
        print("Запуск отрисовки ручкой")


class Pencil(Stationery):
    def draw(self):
        print("\nРодительский метод класса Pencil")
        print("Запуск отрисовки карандашом")


class Handle(Stationery):
    def draw(self):
        print("\nРодительский метод класса Handle")
        print("Запуск отрисовки маркером")


s = Stationery()
print(s.title)
s.draw()

p_1 = Pen()
p_1.draw()

p_2 = Pencil()
p_2.draw()

h = Handle()
h.draw()
