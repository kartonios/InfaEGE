'Задача 23 статград'
# def f(s, end):
#     if s == end:
#         return 1
#     if s > end or s == 11 or s == 15:
#         return 0
#     return f(s+1, end)+ f(s*2,end)+ f(s+3,end)
#
#
# print(f(2,8)*f(8,20))


'23'
# def f(s, end, c, n):
#     if s == end and c <= n:
#         return 1
#     if c > n:
#         return 0
#
#     return f(s+1, end, c+1, n) + f(s*2, end, c+1, n) + f(s-3, end, c+1, n)
#
#
# print(f(1, 10, 0, 7))


'23 hard'
# from functools import lru_cache
# @lru_cache(None)
#
# def f(s, end, c1, c):
#     if s == end and c1 == 30:
#         return c
#     if c1 > 30 or s > end:
#         return 999999999999
#
#     return  min(f(s*2, end, c1, c+1), f(s*3, end, c1, c+1), f(s+1, end, c1+1, c+1))
#
# print(f(1, 9217, 0, 0))


'23'
# def f(s, end):
#     if s == end:
#         return 1
#     if s > end or s in [7,17,27,37,47,57]:
#         return 0
#     return f(s+1, end) + f(s+7, end)
#
# print(f(1, 61))

'''
Исполнитель Калькулятор преобразует число, записанное на экране. 
У исполнителя есть три команды, которым присвоены номера:

0. Прибавь 1
1. Умножь на 2
2. Прибавь 3

Первая команда увеличивает число на экране на 1, вторая увеличивает его в два раза, 
nретья – увеличивает на 3. Программа для исполнителя – это последовательность команд. 
Сколько существует программ, которые преобразуют исходное число 5001 
в число 45789 и при этом не содержат двух одинаковых команд подряд?
'''

'23'

# begin = 5001
# end = 45789
#
# a = [[0]*3 for i in range(end+1)]
# a[begin+1][0] = 1
# a[begin*2][1] = 1
# a[begin+3][2] = 1
#
# for x in range(begin, end+1):
#     if x + 1 <= end:
#         a[x+1][0] += a[x][1] + a[x][2]
#     if x * 2 <= end:
#         a[x*2][1] += a[x][0] + a[x][2]
#     if x + 3 <= end:
#         a[x+3][2] += a[x][0] + a[x][1]
#
# print(sum(a[end]))





# from functools import lru_cache
# import sys
# sys.setrecursionlimit(3000)
# @lru_cache(None)
# def f(s, end, c=''):
#     if s == end:
#         return 1
#     if s > end or '00' in c or '11' in c or '22' in c:
#         return 0
#     return f(s+1, end, c+'0') + f(s*2, end, c+'1') + f(s+3, end, c+'2')
#
#
# print(f(5001, 45789))


'23'
# from functools import lru_cache
# @lru_cache(None)
# def f(s, end, k=False, c18=0):
#     if s == 18:
#         c18 += 1
#     if s == end and c18==1:
#         return 1
#     if s > end or s == 33:
#         return 0
#
#     return f(s+1, end, False, c18) + f(s+3, end, False, c18) + f(s*2, end, True, c18) * (not k)
#
#
#
# print(f(2, 51))

'''

Исполнитель Калькулятор преобразует число, записанное на экране. 
У исполнителя есть четыре команды, которым присвоены номера:

прибавь 1
прибавь 2
умножь на 2
умножь на 3

Выполняя первую из них, исполнитель увеличивает число на экране на 1, 
выполняя вторую – увеличивает на 2, выполняя третью – умножает на 2, 
выполняя четвертую – умножает на 3. Сколько существует различных программ, 
преобразующих число 1 в число 55555 
и не содержат двух подряд идущих команд сложения и двух подряд идущих команд умножения?
'''
'23'
# start = 1
# end = 55555
# s = [[0]*4 for i in range(end+1)]
# # m = [[0]*2 for j in range(end+1)]
# s[start+1][0] = 1
# s[start+2][1] = 1
# s[start*2][2] = 1
# s[start*3][3] = 1
#
# for n in range(start, end+1):
#     if n + 1 <= end:
#         s[n+1][0] += s[n][2] + s[n][3]
#     if n + 2 <= end:
#         s[n+2][1] += s[n][2] + s[n][3]
#     if n * 2 <= end:
#         s[n*2][2] += s[n][0] + s[n][1]
#     if n * 3 <= end:
#         s[n*3][3] += s[n][0] + s[n][1]
#
# print(sum(s[end]))


def f(s, n):
    if s == n:
        return 1
    if n == 13 or s > n:
        return 0
    return f(s+1, n)+f(s*2, n)+f(s*3, n)


print(f(3, 8)*f(8, 18))


