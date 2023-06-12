'Задача 5'
# for n in range (1, 1000):
#     s = bin(n)[2:]
#     m = sum(map(int, s))
#     if m % 2 == 0:
#         s += '0'
#         s = '10' + s[2:]
#     if m % 2 != 0:
#         s += '1'
#         s = '11' + s[2:]
#
#     r = int(s, 2)
#     if r > 40:
#         print(n)
#         break


'Задача 5 демо2023'
# for n in range(0, 1000):
#     r = str(bin(n))[2:]
#     if r.count('1') % 2 == 0:
#         r = '10' + r[2:] + '0'
#     else:
#         r = '11' + r[2:] + '1'
#     r = int(r, 2)
#     if r > 40:
#         print(n)
#         break


'Задача 5 статград'

# for n in range(10,1000):
#     numb = []
#     s = str(n)
#     for i in range(len(s)-1):
#         numb.append(int(s[i] + s[i+1]))
#     r = max(set(numb)) - min(set(numb))
#     if r == 44:
#         print(n)
#         break


'Задача 5 Статград'
# def f(N):
#     R = int(N, 2)
#     s = 0
#     while R > 0:
#         s += R % 10
#         R = R // 10
#
#     if s % 2 == 1:
#         return N + '1'
#     else:
#         return N + '0'
#
#
# minR = 999999999999
# for n in range(1000):
#     r = bin(n)[2:]
#     newR = int(f(f(f(r))), 2)
#     if newR > 1028:
#         minR = min(minR, newR)
#
# print(minR)
# 1035

#6 - 204

#7 - 12


'Задача 5 Статград'

from functools import *
from tqdm import tqdm
# @lru_cache(None)
# def f(n):
#     r = bin(n)[2:]
#     ost = sum(list(map(int, str(n)))) % 2
#     r = r + str(ost)
#     return int(r, 2)
#
# def sumd(x):
#     return sum(map(int, str(x)))
#
# def check(y):
#     y_bin = bin(y)[2:]
#     x2 = int(y_bin[:-1], 2)
#     if sumd(x2) % 2 != int(y_bin[-1]):
#         return False
#
#     y = x2
#     y_bin = bin(y)[2:]
#     x1 = int(y_bin[:-1], 2)
#     if sumd(x1) % 2 != int(y_bin[-1]):
#         return False
#
#     y = x1
#     y_bin = bin(y)[2:]
#     x0 = int(y_bin[:-1], 2)
#     return sumd(x0) % 2 == int(y_bin[-1])
#
#
# # k = 0
# # for x in tqdm(range(100)):
# #     print(x, f(f(f(x))))
#
#
# # k = 0
# # for x in tqdm(range(123456789//9, 1987654321//7)):
# #     if f(f(f(x))) in range(123456789, 1987654322):
# #         k += 1
#
# k = 0
# for i in range(1987654322-8, 1987654322):
#     print(i, check(i))
#
# # [123456792, 1987654320] => 233024691
#
# # print(check(123456792), check(1987654320))
# # for y in range(123456789, 1987654322):
# #     if check(123456789):
# #         k += 1
#
# print(k)


'Задача 5'
# def f(numb):
#     n = int(numb, 2)
#     if n%2 == 0:
#         N = 0
#     else:
#         N =1
#
#     chet = 0
#     nechet = 0
#     while n > 0:
#         ost = n%10
#         n //=10
#         if ost % 2 ==0:
#             chet+=1
#         else:
#             nechet+=1
#     if chet > nechet:
#         return numb + '1'
#
#     elif nechet > chet:
#         return numb + '0'
#
#     elif chet == nechet:
#         if N == 0:
#             return numb + '0'
#         else:
#             return numb + '1'
#
# for i in range(123456789-3, 123456789+5):
#
#     print(int(f(f(f(bin(i)[2:]))), 2), i)

'Задача 5 статград'
# def f(n):
#     r = bin(n)[2:]
#     if n % 5 == 0:
#         r = r + bin(5)[2:]
#     else:
#         r = r + '1'
#     n = int(r,2)
#     if n % 7 == 0:
#         r = r + bin(7)[2:]
#     else:
#         r = r + '1'
#
#     return int(r, 2)
#
#
#
# maxN = 0
# for i in range(1000000, 0,-1):
#     if f(i) < 1728404:
#         maxN = max(maxN, i)
# print(maxN)

def f(n):
    r = bin(n)[2:]
    if n % 10 == 8:
        r = '100' + r[3:]
    if n % 10 == 9:
        r = r[:-3] + '110'
    else:
        r = r[:-3] + bin(n%10)[2:]
    return int(r, 2)

for i in range(10, 1000):
    if f(i) == 62:
        print(f(i), i)