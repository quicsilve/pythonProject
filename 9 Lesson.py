grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

grades = (list(grades))
students = (list(students))

students.sort()

x = []
for key in grades:
    x.append(sum(key) / len(key))
#print(x)

Zurnal = dict(zip(students, x))

print(Zurnal)
