# 1 задание

my_list = [2, None, ('a', '1'), 'True', True, 2.5]
for element in range(len(my_list)):
     print(type(my_list[element]))


# 2 задание

user_list = int(input("Введите количество элементов списка "))
my_list = []
i = 0
element = 0
while i < user_list:
    my_list.append(input("Введите значения списка "))
    i += 1

for elem in range(int(len(my_list) / 2)):
        my_list[element], my_list[element + 1] = my_list [element + 1], my_list[element]
        element += 2
print(my_list)


# 3 задание

user_list = ['зима', 'весна', 'лето', 'осень']
user_dict = {1 : 'зима', 2 : 'весна', 3 : 'лето', 4 : 'осень'}
month = int(input("Введите месяц по номеру "))
if month ==12 or month == 1 or month == 2:
        print(user_dict.get(1))
        print(user_list[0])
elif month == 3 or month == 4 or month == 5:
    print(user_dict.get(2))
    print(user_list[1])
elif month == 6 or month == 7 or month == 8:
    print(user_dict.get(3))
    print(user_list[2])
elif month == 9 or month == 10 or month == 11:
    print(user_dict.get(4))
    print(user_list[3])


# 4 задание

user_str = input('Введите предложение ')
my_str = user_str.split(' ')
for i, el in enumerate(my_str, 1):
    if len(el) >> 10:
        el = el[0:10]
    print(f"{i} ) {el}")


# 5 задание


my_list = [7, 5, 3, 3, 2]
user_number = int(input('Введите число '))
result_list = my_list.count(user_number)
for element in my_list:
    if result_list > 0:
        i = my_list.index(user_number)
        my_list.insert(i+result_list, user_number)
        break
    else:
        if user_number > element:
            j = my_list.index(element)
            my_list.insert(j, user_number)
            break
        elif user_number < my_list[len(my_list) - 1]:
            my_list.append(user_number)
print(my_list)



