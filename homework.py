# 1 задание

age = str(27)
name = 'Катя'
city = 'Екатеринбурга'
print('Привет' ','  'меня зовут ' + name + ' я из ' + city + ' мне '+ age + ' лет')
user_age = int(input('Введите Ваш возраст '))
user_name = input('Введите Ваше имя ')
user_city = input('Из какого Вы города? ')
print(f'Ваше имя: {user_name} Ваш возраст: {user_age} Вы из города {user_city}')
print(input('Все верно? '))


# 2 задание

user_sec = int(input('Введите время в секундах '))
hour = user_sec // 3600
minute = user_sec % 3600 // 60
second = user_sec % 3600 % 60
print(f'ВРЕМЯ {hour}:{minute}:{second}')



# 3 задание

n = int(input('ВВедите число '))
result = (n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n)))
print(f'итого:  {result}')


# 4 задание

n = int(input('Введите целое положительное число '))
m = 0
while n > 0:
    if n % 10 > m:
        m = n % 10
    n = n // 10
print(m)


# 5 задание

revenue = int(input('значение выручки '))
costs = int(input('издержки фирмы '))
if revenue > costs:
    profitability = revenue - costs
    profit_revenue = profitability / revenue
    print(f'фирма отработала с прибылью {profitability}')
    profit_employee = int(input('численность сотрудников фирмы '))
    print(f'прибыль фирмы в расчете на одного сотрудника составляет {profitability / profit_employee}')
elif revenue == costs:
    print('фирма работает в ноль')
else:
    print('фирма работает в убыток')

# 6 задание

a = float(input("сколько пробежали киллометров в первый день?: "))
b = float(input("сколько пробежали киллометров в последний день?: "))
day = 1
while b - a > 0:
    a = a + (a * 0.1)
    day += 1
print(day)