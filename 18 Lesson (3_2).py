#1

def print_params(a = 1, b = str, c = True):
    print(a, b, c)
chislo_b = 25
chislo_c = [1,2,3]
print_params(1, chislo_b, chislo_c )

#2

values_list = (52, False, 5.2 )
values_dict = {'a': 52, 'b': False, 'c': 5.2}
print_params(*values_list)
print_params(**values_dict)

#3

values_list_2 = ("Jony", 0)
print_params(*values_list_2)