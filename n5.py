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
@lru_cache(None)
def f(n):
    r = bin(n)[2:]
    ost = sum(list(map(int, str(n)))) % 2
    r = r + str(ost)
    return int(r, 2)

def sumd(x):
    return sum(map(int, str(x)))

def check(y):
    y_bin = bin(y)[2:]
    x2 = int(y_bin[:-1], 2)
    if sumd(x2) % 2 != int(y_bin[-1]):
        return False

    y = x2
    y_bin = bin(y)[2:]
    x1 = int(y_bin[:-1], 2)
    if sumd(x1) % 2 != int(y_bin[-1]):
        return False

    y = x1
    y_bin = bin(y)[2:]
    x0 = int(y_bin[:-1], 2)
    return sumd(x0) % 2 == int(y_bin[-1])


# k = 0
# for x in tqdm(range(100)):
#     print(x, f(f(f(x))))


# k = 0
# for x in tqdm(range(123456789//9, 1987654321//7)):
#     if f(f(f(x))) in range(123456789, 1987654322):
#         k += 1

k = 0
for i in range(1987654322-8, 1987654322):
    print(i, check(i))

# [123456792, 1987654320] => 233024691

# print(check(123456792), check(1987654320))
# for y in range(123456789, 1987654322):
#     if check(123456789):
#         k += 1

print(k)