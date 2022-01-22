# 1

class Matrix:
    def __init__(self, list_of_lists):
        self.mat = list_of_lists

    def __str__(self):
        string = ''
        for i in self.mat:
            for j in i:
                string = string + '%s\t' % (j)
            string = string[:-1]
            string = string + '\n'
        string = string[:-1]
        return string

    def __add__(self, other):
        result = []
        numbers = []
        for i in range(len(self.mat)):
            for j in range(len(self.mat[0])):
                summa = other.mat[i][j] + self.mat[i][j]
                numbers.append(summa)
                if len(numbers) == len(self.mat[0]):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)


a = [[3, 5, 4], [2, 4, 6], [-1, 11, -7]]
b = [[2, 3, 3], [-2, 1, -5], [5, -3, 0]]
m = Matrix(a)
mm = Matrix(b)

print("\n1-ая матрица")
print(m.__str__(), "\n")

print("2-ая матрица")
print(mm.__str__(), "\n")

print("Сумма двух матриц")
print(m + mm)

# 2

class Clothes:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def pog_m_c(self):
        return self.width / 6.5 + 0.5

    def pog_m_j(self):
        return self.height * 2 + 0.3

    @property
    def pog_m_full(self):
        return str(f'Всего ткани \n'
                   f' {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')


class Coat(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.pog_m_c = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'количество ткани на пальто {self.pog_m_c}'


class Jacket(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.pog_m_j = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'количество ткани на костюм {self.pog_m_j}'

coat = Coat(1, 2)
jacket = Jacket(3, 4)

print(coat)
print(jacket)
print(coat.pog_m_full)
print(jacket.pog_m_full)
print(jacket.pog_m_c())
print(jacket.pog_m_j())



