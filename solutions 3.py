import math
def ex1(file):
    x = open((file)).readline()
    op = -1
    mx = 0
    for c in range(0, x.count('(')):
        op = x.find('(', op+1) # индекс открывающей скобки
        cl = x.find(')', op) # индекс соотв. закрывающей
        if x[op+1] == '+' or x[cl-1] == '+' or x [op+1] == '(':
            None # соблюдение условий, кроме '++' (в т.ч. наличие нескольких скобок "(((..)")
        else:
            fin = 0 # значение после выполнения сложения внутри последовательности
            exp = x[op+1:cl] # содержимое скобок
            for obj in exp.split('+'):
                if obj == '': # если встречается '++', в массиве появляется пустой элемент
                    exp = ''
                    break
                fin += int(obj) # суммирование элементов массива, содержащего числа в скобках
            if fin % 2 == 0:
                if mx < len(exp)+2:
                    mx = len(exp)+2
    print(mx)
def ex2():
    a, b = format(int('7FFFAFF', 16), 'b'), format(int('777727773', 8), 'b')
    # 16: *x16 1010 *x8 -- 28 разрядов
    # 8: *x12 010 *x9 011 -- 27 разрядов
    # выводы: шестнадцатеричное число начинается с 0-7 ради соответствия числа двоичных разрядов
    z = ''
    for x in range(0, len(a)):
        z += str(int(a[x]) & int(b[x]))
    # путём конъюнкции можно сделать вывод, что числа должны соответствовать маске *x12 0101010 *x5 011
    # тогда свободно 17 разрядов, первые 3 не должны соответствовать '000' (условие про значимость, т.к.
    # на конце нет нулей, а разряды между первым и последним всегда значимы, достаточно проверить это)
    # следовательно количество таких чисел можно найти следующим образом:
    print((2**3-1)*2**14)
def ex3(file):
    f = open(file).readline().split()
    maxcount, max, qua, sum = 0, 0, 0, 0
    for m in f: # поиск максимального числа с наиб. кол-вом уникальных цифр
        count = len(set(m))
        if maxcount <= count:
            maxcount = count
            if max < int(m):
                max = int(m)
    for x in range(0, len(f)-2): # перебор троек
        sumduo = 0
        duo = f[x:x+3]
        for n in range(0, 3):
            if int(f[x+n]) >= 0 and math.sqrt(int(f[x+n])).is_integer() == True: # проверка условий с учётом неотрицательности (корень)
                perfect = f[x+n]
                duo.remove(perfect)
        if len(duo) == 2:
            for elem in duo:
                sumduo += int(elem)
            if sumduo > max:
                qua += 1
                sum += int(perfect)
    print(qua, sum)