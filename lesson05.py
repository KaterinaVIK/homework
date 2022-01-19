# 1

my_f = open('test.txt', 'w')
line = input('Введите текст \n')
while line:
    my_f.writelines(line)
    line = input('Введите текст \n')
    if not line:
        break

my_f.close()
my_f = open('test.txt', 'r')
content = my_f.readlines()
print(content)
my_f.close()

# 2

my_file = open('test2.txt', 'r')
content = my_file.read()
print(f'Информация в файле: \n {content}')
my_file = open('test2.txt', 'r')
content = my_file.readlines()
print(f'Количество строк в файле: \n {len(content)}')
my_file = open('test2.txt', 'r')
content = my_file.readlines()
for i in range(len(content)):
    print(f'Количество символов: \n {len(content[i])}')
my_file = open('test2.txt', 'r')
content = my_file.read()
content = content.split()
print(f'Общее количество слов: \n {len(content)}')
my_file.close()

# 5


with open('file_4.txt', 'w+') as file_obj:
    line = input('Введите числа через пробел \n')
    file_obj.writelines(line)
    user_number = line.split()
    print(sum(map(int, user_number)))



