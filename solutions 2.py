from itertools import product, permutations
from functools import lru_cache

def ex1():
    @lru_cache(maxsize=None)
    def f(s, l):
        if l == 0:
            return bin(s).count('1') <= 1
        return sum(f(s ^ (1 << x), l - 1) for x in range(8))
    result = (f(0, 27) - f(1, 26)) % (10**9 + 7)
    print(result)
def ex2():
    dictofnumbers = {} # словарь, где значение - число, а ключ - количество простых
    for number in range(100, 1000):
        primes = 0 # переменная отвечающая за количество простых чисел для каждого трёхзначного
        twodigits = list(permutations(str(number), 2)) # составление двухзначных чисел
        for elem in twodigits:
            dividers = 0 # количество делителей для числа (можно было через break, но.. почему бы и нет)
            twodigit = int(''.join(elem))
            for x in range(2, twodigit): # проверка на наличие делителей
                if twodigit % x == 0:
                    dividers += 1
            if dividers == 0:
                primes += 1
        dictofnumbers.update({primes: number}) # добавление в словарь
    print(dictofnumbers.get(max(dictofnumbers.keys())))
def ex3():
    # Функция для увеличения числа на 1
    def inc(x):
        return x + 1

    # Функция для вычисления суммы делителей числа
    def sumofdividers(x):
        if x == 0:
            return 0
        return sum(num for num in range(1, x + 1) if x % num == 0)

    # Мемоизация для хранения количества путей до каждого числа
    @lru_cache(maxsize=None)
    def count_paths(current, target):
        if current == target:
            return 1  # Нашли один путь
        if current > target:
            return 0  # Превысили целевое число, путь не подходит
        # Рекурсивно считаем пути для обеих команд
        return count_paths(inc(current), target) + count_paths(sumofdividers(current), target)

    # Вычисляем количество путей от 2 до 24
    result = count_paths(2, 24)
    print(result)
def ex4():
    for i in range(10**5,2*10**7): #ограничения обусловлены простыми логическими умозаключениями:
        #нижняя граница - т.к. делитель 22768, а начинается с 1 - больше 100000
        #верхняя граница - т.к. начинается с 1, а 10**8 не подходит, достаточно рассмотреть до 2*10**7
        s=str(i)
        if s[0] == '1' and '03' in s[1:] and '6' in s[s.index('03')+1:]: # проверка первичных условий
            if s.index('03') > 1: # проверка на то, является ли N пустой последовательностью
                N = int(s[1:s.index('03')]) # декларация N как переменной, равной отрывку от 1 до 03
                for m in range(2, N):
                    if N % m == 0:
                        if int(s) % 22768 == 0:
                            print(s, N)
                        break
                    else:    
                        None
            else:
                if int(s) % 22768 == 0:
                    print(s)
