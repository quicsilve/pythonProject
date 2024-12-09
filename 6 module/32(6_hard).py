# Дополнительное практическое задание по модулю: "Наследование классов."
# Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности
# Задание "Они все так похожи":
# 2D? 3D? Даже 4D?.... Настолько глубоко мы заходить конечно же не будем, 4D подождёт, но вот с двумерными и трёхмерными фигурами можем поэкспериментировать.
# Вы когда-нибудь задумывались как устроены графические библиотеки для языков программирования?
# Безусловно, там выполняются огромные расчёты при помощи вашей видеокарты, но... Что лежит в основе удобного использования таких объектов?
# По названию задачи можно понять, что все геометрические фигуры обладают схожими свойствами, такими как: длины сторон, цвет и др.
# Давайте попробуем реализовать простейшие классы для некоторых таких фигур и при этом применить наследование (в будущем, изучая сторонние библиотеки, вы будете замечать схожие классы, уже написанные кем-то ранее):
# Общее ТЗ:
# Реализовать классы Figure(родительский), Circle, Triangle и Cube, объекты которых будут обладать методами изменения размеров, цвета и т.д.
# Многие атрибуты и методы должны быть инкапсулированны и для них должны быть написаны интерфейсы взаимодействия (методы) - геттеры и сеттеры.
# Подробное ТЗ:
# Атрибуты класса Figure: sides_count = 0
# Каждый объект класса Figure должен обладать следующими атрибутами:
# Атрибуты(инкапсулированные): __sides(список сторон (целые числа)), __color(список цветов в формате RGB)
# Атрибуты(публичные): filled(закрашенный, bool)
# И методами:
# Метод get_color, возвращает список RGB цветов.
# Метод __is_valid_color - служебный, принимает параметры r, g, b, который проверяет корректность переданных значений перед установкой нового цвета. Корректным цвет: все значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно).
# Метод set_color принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие значения, предварительно проверив их на корректность. Если введены некорректные данные, то цвет остаётся прежним.
# Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон, возвращает True если все стороны целые положительные числа и кол-во новых сторон совпадает с текущим, False - во всех остальных случаях.
# Метод get_sides должен возвращать значение я атрибута __sides.
# Метод __len__ должен возвращать периметр фигуры.
# Метод set_sides(self, *new_sides) должен принимать новые стороны, если их количество не равно sides_count, то не изменять, в противном случае - менять.
# Атрибуты класса Circle: sides_count = 1
# Каждый объект класса Circle должен обладать следующими атрибутами и методами:
# Все атрибуты и методы класса Figure
# Атрибут __radius, рассчитать исходя из длины окружности (одной единственной стороны).
# Метод get_square возвращает площадь круга (можно рассчитать как через длину, так и через радиус).
# Атрибуты класса Triangle: sides_count = 3
# Каждый объект класса Triangle должен обладать следующими атрибутами и методами:
# Все атрибуты и методы класса Figure
# Метод get_square возвращает площадь треугольника. (можно рассчитать по формуле Герона)
# Атрибуты класса Cube: sides_count = 12
# Каждый объект класса Cube должен обладать следующими атрибутами и методами:
# Все атрибуты и методы класса Figure.
# Переопределить __sides сделав список из 12 одинаковы сторон (передаётся 1 сторона)
# Метод get_volume, возвращает объём куба.
# ВАЖНО!
# При создании объектов делайте проверку на количество переданных сторон, если сторон не ровно sides_count, то создать массив с единичными сторонами и в том кол-ве, которое требует фигура.
# Пример 1: Circle((200, 200, 100), 10, 15, 6), т.к. сторона у круга всего 1, то его стороны будут - [1]
# Пример 2: Triangle((200, 200, 100), 10, 6), т.к. сторон у треугольника 3, то его стороны будут - [1, 1, 1]
# Пример 3: Cube((200, 200, 100), 9), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [9, 9, 9, ....., 9] (12)
# Пример 4: Cube((200, 200, 100), 9, 12), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [1, 1, 1, ....., 1]

class Figure:
    SIDES_COUNT = 0

    def __init__(self, color, *sides, filled):
        self.__sides = sides
        self.__color = list(color)
        self.filled = filled
        if not self.__is_valid_sides(*self.__sides):
            self.__sides = (1) * self.SIDES_COUNT  # Если не прошли проверку сторон, то все длины сторон 1
        elif isinstance(self, Cube):
            self.__sides = sides * self.SIDES_COUNT  # Размножаем одну сторону для куба
        if not self.__is_valid_color(*self.__color):
            self.__color = [255, 0, 0]  # Если не прошли проверку по цвету, то цвет КРАСНЫЙ

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if (0 <= r <= 255) and (0 <= g <= 255) and (0 <= b <= 255):
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *args):  #  - Служебный, принимает неограниченное кол-во сторон, возвращает True если все стороны целые положительные числа и кол-во новых сторон совпадает с текущим
        if isinstance(self, Cube):
            sd_cnt = 1
        else:
            sd_cnt = self.SIDES_COUNT
        sides_bool = True
        for side in args:
            if (not isinstance(side, int)) or (side < 0) or (len(args) != sd_cnt):
                sides_bool = False
                break
        return sides_bool

    def get_sides(self):  
        return list(self.__sides)

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):  
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
        else:
            print(f'Стороны не удовлетворяют требованиям.')

class Circle(Figure):
    SIDES_COUNT = 1

    def __init__(self, color, *sides, filled=False):
        from math import pi
        super().__init__(color, *sides, filled=filled)
        self.__radius = self.get_sides()[0] / (2 * pi)

    def get_square(self):
        from math import pi
        return list(pi * self.__radius ** 2)

    def get_radius(self):
        return list(self.__radius)

    def set_sides(self, *new_sides):  
        from math import pi
        super().set_sides(*new_sides)
        self.__radius = self.get_sides()[0] / (2 * pi)

class Triangle(Figure):
    SIDES_COUNT = 3

    def __init__(self, color, *sides, filled=False):
        super().__init__(color, *sides, filled=filled)
        self.__trng_check()

    def get_square(self):
        sides = self.get_sides()
        # формула Герона для площади треугольника
        p = sum(sides) * 0.5
        return (p * (p - sides[0]) * (p - sides[1]) * (p - sides[2])) ** 0.5

    def check(self):  # Проверка возможности создания треугольника с такими сторонами
        a = self.get_sides()[0]
        b = self.get_sides()[1]
        c = self.get_sides()[2]
        if (a + b) < c or (a + c) < b or (c + b) < a:
            print(f'Невозможно создать треугольник с такими сторонами: {self.get_sides()}')
            self.set_sides(1, 1, 1)

class Cube(Figure):
    SIDES_COUNT = 12

    def __init__(self, color, *sides, filled=False):
        super().__init__(color, *sides, filled=filled)

    def get_volume(self):
        return self.get_sides()[0] ** 3

# Код для проверки:
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())