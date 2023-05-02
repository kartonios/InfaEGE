'задача 16'
# from math import factorial
# from tqdm import *          # не идет в стоке!!! необходима установка
# from functools import *
#
# @lru_cache(maxsize=none)
# def f(n):
#     if n == 0:
#         return 0
#     if n % 3 != 0:
#         return f(n - 1) + 1
#     if n > 0 and n % 3 == 0:
#         return f(n//3)


'задача 16.42'
# def f(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return f(n-1) + 3 * g(n-1)
#
#
# def g(m):
#     if m == 1:
#         return 1
#     if m > 1:
#         return f(m-1) - 2 * g(m-1)
#
#
# print(f(18))  #ответ: 18298549
# s = sum(map(int, str(x)))       #сумматор


'задача 16.58'
# def f(n):
#     if n > 30:
#         return n * n + 3 * n + 5
#     if n <= 30 and n % 2 == 0:
#         return 2 * f(n+1) + f(n+4)
#     if n <= 30 and n % 2 != 0:
#         return f(n+2) + 3 * f(n+5)
#
#
# res = 0
# for i in range(1, 1001):
#     if str(f(i)).count('0') >= 2:
#         res+=1
#
# print(res)  #ответ: 77
#
#
# print(max({f(x) for x in range(1200000000, 1600000001)}))
# for x in tqdm(range(1200000002, 1600000001, 3)):
#     y = f(x)
#     # print(x, y)
#
# res = set()
# for y in range(34642):
#     for k in range(1, 32):
#         x = (3*y + 2) ** k
#         if 1200000000 <= x <= 1600000000:
#             print(x)
#             res.add(f(x))
#         elif x > 1600000000:
#             break
#
# print(max(res), res)
#
# def f(x):
#     if x != 30 and f(x) + 0.9*f((30*x+2)/(x-30))== 7*x:
#         return 1
#     else:
#         return none
#
# print(f(1))



'задача 16 статград'

# def f(n):
#     if n % 2 == 0:
#         return (1 + n) * (n // 2)
#     else:
#         return f(n-1) + n
#
# res =[]
#
#
# for N in [237567892, 237567893, 237567894, 1134567002, 1134567003, 1134567004]:
#     num = f(N)
#     if num % 3 != 0:
#         res.append((N, num))
#
# print(res)   #298 999 706


'задача 16'
# def f(n):
#     if n == 0:
#         return 0
#     return f(n // 10) + (n % 10)
#
#
#
# def f2(N):
#     return sum(map(int, str(N)))
#
# start = 237567892
# stop = 1134567009+1
# last = f2(1)
# k = 0
# # for i in range(237567892+1, 1134567010):
# # for i in range(start, stop + 1):
# #     new = f2(i)
# #     if last > new:
# #         k+=1
# #         print(i-1, i, "|", last, new)
# #     last = new
# #
# # print(k)
#
# print((stop // 10) - (start // 10))
# print(stop - start + 1)


'задача 16'
# def f(a, b):
#     if a == 0 and b == 0:
#         return 0
#
#     if a > b:
#         return f(a-1, b) + b
#
#     if a <= b and b > 0:
#         return f(a, b-1) + a
#
# k = 0
# for a in range(10):
#     for b in range(10):
#         print(a, b, f(a, b))


'Задача 16 статград'
# def f(a, b):
#     if b == 0:
#         return a
#
#     elif a >= b > 0:
#         return f(a-b, b)
#
#     elif a < b:
#         return f(b, a)
#
#
#
# a = []
# for i in range(100):
#     if f(i, 14) == 1:
#         print(i)
#         a.append(i)
#
# print(len(a), (100//12)*6-5)
# print((123456795+1)/7, (123456795-1)/7 )
#
# print((1234567888-123456795-1)-((1234567888-123456795)//7) + ((1234567888-123456795)//14) - ((1234567888-123456795)//2))



'Задача 16 статград'

def f(n):
    if n > 1000000:
        return n
    if n <= 1000000:
        return n+f(2*n)

def g(m):
    return f(m)/m

c = 0
for x in range(1, 10000000):
    if g(x) == 2047:
        c+=1
print(c)
# 977