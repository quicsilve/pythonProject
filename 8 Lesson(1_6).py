my_dict = {'Evgen': 2003,'Howard': 2003}
print(my_dict)
print(my_dict.get('Dora', 'К сожалению у тебя нет ее даты в телефоне ^_^'))
my_dict['Stark'] = 1990
my_dict.update ({'Natasha': 1996})
del my_dict['Howard']
print(my_dict)


#my_set = {52, 52, 'SPb', 'SPb', True}
my_set = [52, 52, 'SPb', 'SPb', True, 5.2, 5.3]
my_set = set(my_set)
print(my_set)
print(my_set.discard(52))
print(my_set)
