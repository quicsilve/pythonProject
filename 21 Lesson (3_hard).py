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