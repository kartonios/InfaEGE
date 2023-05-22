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


'23################################################################'
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
from functools import lru_cache
@lru_cache(None)
def f(s, end, k=False, c18=0):
    if s == 18:
        c18 += 1
    if s == end and c18==1:
        return 1
    if s > end or s == 33:
        return 0

    return f(s+1, end, False, c18) + f(s+3, end, False, c18) + f(s*2, end, True, c18) * (not k)



print(f(2, 51))