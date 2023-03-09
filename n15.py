'Задача 15 Демо'
# def dell(n,m):
#     return n % m == 0
#
# # for a in range(1, 1001):
# #     all_good = True
# #     for x in range(1, 1001):
# #         if ((not dell(x,2) or not dell(x, 3)) or (x + a >= 100)) == False:
# #             all_good = False
# #             break
# #
# #     if all_good:
# #         print(a)
# #         break
#
# for a in range(1, 1001):
#     for x in range(1, 1001):
#         if ((not dell(x,2) or not dell(x, 3)) or (x + a >= 100)) == False:
#             break
#     else:
#         print(a)
#         break
# else:
#     print('no A exist, change ranges')


'Задача 15.25'
# for a in range(1, 1001):
#     for x in range(1, 1001):
#         if ((x & 125 != 1) or (not (x & 34 == 2) or (x & a == 0))) == False:
#             break
#
#     else:
#         print(a)
#         break


'Задача 15.18'
# def check(A):
#     for x in range(1, 1001):
#         for y in range(1, 1001):
#             if ((not (x<=9) or (x*x<=A)) and (not (y*y<=A) or (y<=9))) == False:
#                 return False
#     else:
#         return True
#
#
#
# for a in range(1001, 1, -1):
#     if check(a) == True:
#         print(a)
#         break


'Задача 15.14'
# from itertools import *
#
# b = {2, 4, 6, 8, 10, 12}
# c = {4, 8, 12, 116}
# bc = b | c
#
# for L in range(1, len(bc)+1):
#     for a in combinations(bc, L):
#         for x in range(160):
#             if (not (x in b) or (not ((x in c) and not (x in a)) or not (x in b))) == False:
#                 break
#         else:
#             print(sum(a))
#             break

'Задача 15'
# def d(n, m):
#     return n % m == 0
#
# def check(a):
#     for x in range(1, 1000):
#         for y in range(1, 1000):
#             if ((not d(144, x) or not d(x, y)) or (x + y > 100) or (a - x > y)) == 0:
#                 return 0
#     else:
#         return 1
#
#
#
# for a in range(1, 1000):
#     if check(a) == 1:
#         print(a)
#         break


'Задача 15'
# for A in range(1, 1000):
#     for x in range(1000):
#         if ((x&51 == 0) or (not(x&41 == 0) or (x&A == 0))) == 0:
#         # if (not((x&28 != 0) or (x&45 != 0)) or (not(x&48 == 0) or x&A != 0)) == 0:
#             break
#     else:
#         print(A)


'Задача 15'
# P = [i for i in range(10, 16)]
# Q = [i for i in range(10, 21)]
# R = [i for i in range(5, 16)]
#
# maxA = 0
# minA = 99999999999999999
# for s in range(1000):
#     for end in range(s, 1000):
#         A = [i for i in range(s, end)]
#         for x in range(100):
#             if (not(x in A) or (x in P)) != (not(x in Q) or (x in R)):
#                 break
#             # if ((not(x in A) or (x in P)) or (x in Q)) == 0:
#             #     break
#         else:
#             minA = max(minA, len(A))
#             print(minA)
#             # maxA = max(maxA, len(A)-1)
#             # print(maxA)


'Задача 15'
# for A in range(1000):
#     for x in range(1000):
#         if (not((x&35 != 0) or(x&22 !=0)) or (not(x&15 == 0) or (x&A != 0))) == 0:
#             break
#     else:
#         print(A)
#         break


'Задача 15'
p = [i for i in range(18, 23)]
q = [i for i in range(12, 31)]
r = [i for i in range(23, 46)]

for a_start in range(12, 100):
    for a_end in range(a_start+1, 100):
        # a = [i for i in range(a_start, a_end+1)]
        for xx in range(10, 200):
            x = xx/2
            if ((a_start <= x <= a_end) or (17 < x < 23)) == (not(12 <= x <= 30) or (23 <= x <= 45)):
                break
        else:
            print(a_start, a_end)

# print(sorted(a), len(a))

