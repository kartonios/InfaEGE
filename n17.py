'Задача 17 Демо'
# Остаток от деления на отрицательное число высчитывается по формуле pq + r,

# st = open(r"C:\Users\karton\Desktop\EGE\demo2023_files\Задание 17\17.txt").read().splitlines()
# a = list(map(int, st))
# max3 = -10001
# max_sqrt_pair = 0
# res = 0
# for i in range(len(a)):
#     if abs(a[i]) % 10 == 3 and a[i] > max3:
#         max3 = a[i]
#
#
# print(max3)
# for index in range(len(a) - 1):
#     # f = int(st[index])
#     # s = int(st[index + 1])
#     f = a[index]
#     s = a[index+1]
#     s2 = f**2 + s**2
#     if (((f % 10 == 3) and (s % 10 != 3)) or ((f % 10 != 3) and (s % 10 == 3))) and s2 >= max3**2:
#         max_sqrt_pair = max(max_sqrt_pair, s2)
#         res += 1
#
#
#
#
# print(res, max_sqrt_pair)


# i i+1 --> range(0, n-1)
# i-1 <-i --> range(1, n)
# 0 1 2 3 4
# 0 1
#   1 2
#     2 3
#       3 4

# st = open(r"C:\Users\karton\Desktop\EGE\demo2023_files\Задание 17\17.txt").read().splitlines()
# s = list(map(int, st))
# res = 0
# max2 = -100000
# maxPair = 0
#
# for i in s:
#     if abs(i) % 10 == 3 and i > max2:
#         max2 = i
#
# print(max2, max2**2)
# for n in range(len(s) - 1):
#     f = abs(s[n])
#     c = abs(s[n + 1])
#     sum2 = f**2 + c**2
#     if ((f % 10 == 3) != (c % 10 == 3)) and sum2 >= max2**2:
#         maxPair = max(maxPair, sum2)
#         res +=1
#
# print(res, maxPair)


'Задача 17.250'
# st = open(r"C:\Users\karton\Desktop\EGE\17\17-243.txt").read().splitlines()
# a = list(map(int, st))
# maxN = 0
# minPair = 9999999
# pairs = 0
# for i in range(len(a)):
#     if a[i] % 171 == 0 and a[i] > maxN:
#         maxN = a[i]
#
#
# for x in range(len(a)-1):
#     f = a[x]
#     s = a[x+1]
#     if ((f > maxN or s > maxN) and (('11' in str(f)) or ('11' in str(s)))):
#         pairs+=1
#         minPair = min(minPair, f+s)
#
#
# print(pairs, minPair)
"""Ответ: 25 10899"""



'Задача 17.238'
# l = open(r"C:\Users\karton\Desktop\EGE\17\17-1.txt").read().splitlines()
# a = list(map(int, l))
# mean = sum(a) // len(a)
# maxTriple = 0
# triples = 0
#
# for i in range(len(a)-2):
#     less = 0
#     f = a[i]
#     s = a[i-1]
#     t = a[i-2]
#     if f < mean: less+=1
#     if s < mean: less+=1
#     if t < mean: less+=1
#     if less >= 2 and ((f % 100 == 14) or (s % 100 == 14) or (t % 100 == 14)):
#         triples+=1
#         maxTriple = max(maxTriple, f+s+t)
#
#
# print(triples, maxTriple)
"""Ответ 160 3980"""



'Задача 17.257'
# l = open(r"C:\Users\karton\Desktop\EGE\17\17-257.txt").read().splitlines()
# a = list(map(int, l))
# min7 = 9999999
# min13 = 9999999
# all7 = 0
# all13 = 0
#
# for i in range(len(a)):
#     if a[i] % 7 == 0:
#         all7+=1
#         min7 = min(min7, a[i])
#
#     if a[i] % 13 == 0:
#         all13+=1
#         min13 = min(min13, a[i])
#
# if min7 > min13:
#     print(all7, min7)
# else:
#     print(all13, min13)
"""Ответ 92 299"""

'Задача 17 статград'
# l = list(map(int, open(r'D:\downloads\17.txt').readlines()))
# minsqrt = min([x for x in l if str(x)[-2] == str(x)[-1]])**2
# pairs = 0
# maxsqrt = 0
#
# for i in range(len(l)-1):
#     f = abs(l[i])
#     s = abs(l[i+1])
#     if str(f)[-1] == str(s)[-2] or str(f)[-2] == str(s)[-1]:
#         if (f % 7 == 0) != (s % 7 == 0):
#             if f**2 + s**2 <= minsqrt:
#                 pairs+=1
#                 maxsqrt = max(maxsqrt, f**2 + s**2)
#
#
# print(pairs, maxsqrt)


'17 статград'
# l = list(map(int, open(r"C:\Users\karton\Desktop\InfaEGE\ege\stat202304_files\17.txt").read().split()))
# min5 = 99999
# pairs = 0
# m = 0
#
# for n in l:
#     if len(str(n)) == 3 and n % 10 == 5:
#         min5 = min(min5, n)
#
# for x in range(len(l)-1):
#     f = l[x]
#     s = l[x+1]
#     if (len(str(f)) == 4 and len(str(s)) != 4) or (len(str(f)) != 4 and len(str(s)) == 4):
#         if (f**2 + s**2) % min5 == 0:
#             pairs+=1
#             m = max(m, f**2 + s**2)
# print(pairs, m)


'17'
a = [int(x) for x in open('112.txt')]
min53 = min([x for x in a if 99 < x < 1000 and x % 10 == 5])
r = []
count = 0
for i in range(len(a)-1):
    a1 = a[i]
    a2 = a[i+1]
    if ((99 < a1 < 1000) or (99 < a2 < 1000)) and ((a1+a2) % min53 == 0):
        r.append(a1+a2)
        count += 1

print(count, max(r))
