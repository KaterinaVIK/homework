
# 1 задание

def res (a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print(f'На ноль делить нельзя')

print(res(int(input('первое значение ')), int(input('второе значение ')))))


# 2 задание

def user(name, lastname, year_of_birth, city, email, phone):
    return print(f'Ваше Имя: {name} Фамилия: {lastname} Год рождения: {year_of_birth}'
                 f'Город проживания: {city} Email: {email} Телефон: {phone}')

user(name=input('Имя: '),
    lastname=input('Фамилия: '),
    year_of_birth=input('Год Рождения: '),
    city=input('Город проживания: '),
    email=input('email: '),
    phone=input('phone: '),)


# 3 задание

def my_func(arg1, arg2, arg3):
    print(f'Сумма двух наибольших аргументов равна: {arg1 + arg2 + arg3 - min([arg1, arg2, arg3])}')


my_func(int(input('Аргумент 1:')),
        int(input('Аргумент 2:')),
        int(input('Аргумент 3:')),)


# 4 задание

def my_func(x, y):
    return 1 / x ** abs(y)

print(f'{my_func(int(input("Возвести число Х: ")), int(input("В степень Y: ")))}')





