# 1 задание

from sys import argv

p1, p2, p3 = map(int, argv[1:])
res = (p1 * p2 + p3)
print(f"зп сотрудника {res}")


# 2 задание

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [el for i, el in enumerate(my_list) if my_list[i - 1] < my_list[i]]
print(new_list)

# 3 задание

print(f'Числа от 20 до 240 кратные 20 или 21:'
      f'{[el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]}')


# 4 задание

my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [el for el in my_list if my_list.count(el) == 1]
print(new_list)

# 5 задание


from functools import reduce
my_list = [el for el in range(99, 1001) if el % 2 == 0]
def my_func(prev_el, el):
    return prev_el * el

print(reduce(my_func, my_list))

# 6 задание


from itertools import count, cycle

for i in count(2):
    print(i)
    if i > 10:
        break

j = 0
for el in cycle('meow'):
    print(el)
    j+=1
    if j > 10:
        break




