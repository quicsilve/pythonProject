# Дополнительное практическое задание по модулю: "Подробнее о функциях."
# Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности
# Задание "Раз, два, три, четыре, пять .... Это не всё?":
# Наши студенты, без исключения, - очень умные ребята. Настолько умные, что иногда по утру сами путаются в том, что намудрили вчера вечером.
# Один из таких учеников уснул на клавиатуре в процессе упорной учёбы (ещё и трудолюбивые). Тем не менее, даже после сна, его код остался рабочим и выглядел следующим образом:
# data_structure = [
#   [1, 2, 3],
#   {'a': 4, 'b': 5},
#   (6, {'cube': 7, 'drum': 8}),
#   "Hello",
#   ((), [{(2, 'Urban', ('Urban2', 35))}])
# ]
# Увидев это студент задался вопросом: "А есть ли универсальное решение для подсчёта суммы всех чисел и длин всех строк?"
# Да, выглядит страшно, да и обращаться нужно к каждой внутренней структуре (списку, словарю и т.д.) по-разному.
# Ученику пришлось каждый раз использовать индексацию и обращение по ключам - универсального решения для таких структур он не нашёл.
# Помогите сокурснику осуществить его задумку.
# Что должно быть подсчитано:
# Все числа (не важно, являются они ключами или значениям или ещё чем-то).
# Все строки (не важно, являются они ключами или значениям или ещё чем-то)
# Для примера, указанного выше, расчёт вёлся следующим образом:
# 1 + 2 + 3 + len('a') + 4 + len('b') + 5 + 6 + len('cube') + 7 + .... + 35 = 99
# Входные данные (применение функции):
# data_structure = [
# [1, 2, 3],
# {'a': 4, 'b': 5},
# (6, {'cube': 7, 'drum': 8}),
# "Hello",
# ((), [{(2, 'Urban', ('Urban2', 35))}])
# ]
# result = calculate_structure_sum(data_structure)
# print(result)
# Выходные данные (консоль):
# 99
# Примечания (рекомендации):
# Весь подсчёт должен выполняться одним вызовом функции.
# Рекомендуется применить рекурсивный вызов функции, для каждой внутренней структуры.
# Т.к. каждая структура может содержать в себе ещё несколько элементов, можно использовать параметр *args
# Для определения типа данного используйте функцию isinstance.

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

#x1 = isinstance([1, 2, 3], list)
#x2 = isinstance({'a': 4, 'b': 5}, dict)
#x3 = isinstance(6, int)
#x4 = isinstance( {'cube': 7, 'drum': 8}, dict)
#x5 = isinstance("Hello", str)
#x6 = isinstance(((), [{(2, 'Urban', ('Urban2', 35))}]), tuple)

#print(x1)
#print(x2)
#print(x3)
#print(x4)
#print(x5)
#print(x6)

def calculate_structure_sum(*items):
  summa = 0
  for i in items:
    
    if isinstance(i, str): # строка
      summa += len(i)

    elif isinstance(i, dict): # словарь
      for key, value in i.items():
        summa += calculate_structure_sum(key, value)

    elif isinstance(i, int) or isinstance(i, float): # число
      summa += i

    elif isinstance(i, (list,tuple,set)): # кортеж
      summa += calculate_structure_sum(*i)

  return summa

    
result = calculate_structure_sum(data_structure)
print(result)