# Задача "Ошибка эволюции":
# Замечали, что некоторые животные в нашем мире обладают странными и, порой, несовместимыми друг с другом свойствами? Например, утконос... Вроде есть клюв, но не птица. Вроде милый, а есть шипы на задних лапах. А ещё он откладывает яйца... Опустим факт о том, что они потеют молоком и попробуем не эволюционным способом создать нашего утконоса.
# Необходимо написать 5 классов:
# Animal - класс описывающий животных.
# Класс обладает следующими атрибутами:
# live = True
# sound = None - звук (изначально отсутствует)
# _DEGREE_OF_DANGER = 0 - степень опасности существа
# Объект этого класса обладает следующими атрибутами:
# _cords = [0, 0, 0] - координаты в пространстве.
# speed = ... - скорость передвижения существа (определяется при создании объекта)
# И методами:
# move(self, dx, dy, dz), который должен менять соответствующие кооординаты в _cords на dx, dy и dz в том же порядке, где множетелем будет являтся speed. Если при попытке изменения координаты z в _cords значение будет меньше 0, то выводить сообщение "It's too deep, i can't dive :(" , при этом изменения не вносяться.
# get_cords(self), который выводит координаты в формате: "X: <координаты по x>, Y: <координаты по y>, Z: <координаты по z>"
# attack(self), который выводит "Sorry, i'm peaceful :)", если степень опасности меньше 5 и "Be careful, i'm attacking you 0_0" , если равно или больше.
# speak(self), который выводит строку со звуком sound.
# Bird - класс описывающий птиц. Наследуется от Animal.
# Должен обладать атрибутом:
# beak = True - наличие клюва
# И методом:
# lay_eggs(self), который выводит строку "Here are(is) <случайное число от 1 до 4> eggs for you"
# AquaticAnimal - класс описывающий плавающего животного. Наследуется от Animal.
# В этом классе атрибут _DEGREE_OF_DANGER = 3.
# Должен обладать методом:
# dive_in(self, dz) - где dz изменение координаты z в _cords. Должен изменять в отрицательную сторону координату z уменьшенную в 2 раза с учётом скорости. С каким бы знаком не был передан параметр dz, внутри метода используйте его значение по модулю (функция abs).
# PoisonousAnimal - класс описывающий ядовитых животных. Наследуется от Animal.
# В этом классе атрибут _DEGREE_OF_DANGER = 8.
# Duckbill - класс описывающий утконоса. Наследуется от классов Bird, AquaticAnimal, PoisonousAnimal. Порядок наследования определите сами, опираясь на ниже приведённые примеры выполнения кода.
# Объект этого класса должен обладать одним дополнительным атрибутом:
# sound = "Click-click-click" - звук, который издаёт утконос

import random

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed
    def move(self, dx, dy, dz):
        pass
    def get_cords(self):
        print(f"X: {self.dx}, Y: {self.dy}, Z: {self.dz}")
    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful")
        elif self._DEGREE_OF_DANGER >= 5:
            print("Be careful, i'm attacking you 0_0")
    def speak(self):
        return self.sound

class Bird(Animal):
    beak = True
    def lay_eggs(self):
        print("Here are (is) {randomint} eggs for you")

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3
    def dive_in(self, dz):
        pass

class PoisonousAnimal(Animal):
     _DEGREE_OF_DANGER = 8

class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    sound = "Click-click-click"
