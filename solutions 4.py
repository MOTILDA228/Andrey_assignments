from itertools import combinations
def ex1(file):
    x = open(file).read()
    counter = 0
    memory = None # идея в том, чтобы сохранять первую встреченную нечётное кол-во раз букву
    alphabet = set(x)
    for letter in alphabet:
        if x.count(letter) % 2 == 1:
            if memory == None:
                memory = letter
            else: # и заменять её следующей такой же, разбивая их на пары 
                memory = None
                counter +=1
    print(counter)

def ex2(file):
    x = open(file).readlines()
    c = int(x.pop(0))
    for num in range(0, c):
        x[num] = int(x[num])
    x.sort()
    cp = []
    for z in range(0, c): 
        for v in combinations(x, z): 
            if sum(v) in cp: None 
            else: cp.append(sum(v)) 
    print(sum(x)-len(cp), max(cp)) # страшно, запускать не рекомендую

# ничего сильно умнее простого перебора мне в голову, к сожалению, не пришло
# мемоизация вряд-ли действительно актуальна т.к. значения повторяются достаточно редко
# print(x) - несложно заметить, что разница между сильно разнящимися по значению группами чисел 
# удобно подходит под начальную (1-24) группу, но что делать с этой информацией понять не могу

def ex3():
    answ = []
    for x in range(0, 18): # границы определены системой счисления первого слагаемого
        for y in range (x+1, 18): # границы определены наличием x во втором слагаемом и y в первом
            if y > 8: # 8 - число, которое должно существовать во втором слагаемом
                sum = (18**3)*5 + 10 + (18**2)*x + y*18 + (y**3) + (y**2)*8 + x*y + 7
                if sum in answ: None
                else: answ.append(sum)
    print(len(answ))
