'Код работает только под СТРАТЕГИЮ -> any(h) if (c+1)%2 == m%2 else all(h)'
'Не строгое условие -> any(h) if (c+1)%2 == m%2 else any(h)'

'статград 19-21'
# def game(a, b, c, m):
#     if c > m:  # если нужно больше m ходов, то киллим процесс
#         return False
#
#     print('\t'*c, a, b, "\t", ("" if a+b <81 else ("V" if  c%2 == m%2 else "X")))
#     if a+b >= 81: #проверяем набралось ли нужно кол-во камней
#         return c <= m and c%2 == m%2
#
#     if a > b: #пул ходов с условием
#         h = [game(a, b+1, c+1, m), game(a, b+2, c+1, m), game(a, b*2, c+1, m)]
#     elif a < b:
#         h = [game(a+1, b, c+1, m), game(a+2, b, c+1, m), game(a*2, b, c+1, m)]
#     else:
#         h = [game(a+1, b, c+1, m), game(a+2, b, c+1, m), game(a*2, b, c+1, m),
#              game(a, b+1, c+1, m), game(a, b+2, c+1, m), game(a, b*2, c+1, m),]
#
#         #если нужный ход, провереям один из ходов, иначе все
#     return any(h) if (c+1)%2 == m%2 else all(h)
#
#
#
# # for b in range(1, 69): #кол-во камней
# #     for m in range(0, 10): #кол-во ходов
# #         if game(12, b, 0, m): #проверка победы на m ходу
# #             if m == 2  or m == 4:
# #                 print(b, m)
# #                 break
# #
# # for b in 49, 50, 55, 56:
# #     print(b, game(12, b, 0, 2), game(12, b, 0, 4))
#
#
#
# #19 - 55
# #20 - 31 54
# #21 - 56


'19.79'
# def f(a, c, m):
#     if c > m:
#         return 0
#     # print("\t" * c, a, '\t', ("V" if a >= 20 and a <= 30 and c%2 == m%2 else ""))
#     if a >= 20 and a <= 30:
#         return c%2 == m%2 and c == m
#     elif a > 30:
#         return c%2 != m%2
#
#     h = [f(a+1, c+1, m), f(a*2, c+1, m)]
#
#     return any(h) if (c+1)%2 == m%2 else all(h)
#
#
# for a in range(1, 20):
#     for m in range(0, 3):
#         if f(a, 0, m):
#             if m == 2:
#                 print(a, m)
#                 break
# #19 - 5
#
#
# # for a in range(1, 20):
# #     for m in range(0, 6):
# #         if f(a, 0, m):
# #             if m == 3:
# #                 print(a, m)
# #                 break
# #20 - 9 17


# for a in range(1, 20):
#     for m in range(0, 6):
#         if f(a, 0, m):
#             if m == 4:
#                 print(a, m)
#                 break
# #21 - 16


'19.47'
# def g(a, c, m, print_move=False):
#     if c > m:
#         return 0
#     if print_move:
#         print('\t' * c, a, "\t", ("" if not(a >= 36 and a <= 60) else ("V" if c % 2 == m % 2 else "X")))
#
#     if a >= 36 and a <= 60:
#         return c % 2 == m % 2
#     elif a > 60:
#         return c % 2 != m % 2
#
#
#
#
#     h = [g(a+1, c+1, m, print_move),
#          g(a*2, c+1, m, print_move),
#          g(a*3, c+1, m, print_move)]
#
#     return any(h) if (c+1)%2 == m%2 else all(h)
#
#
# mass = []
# for i in range(1, 36):
#     for m in range(1, 5):
# #         if g(i, 0, m) and m == 2:
# #             print(i, m)
# #         if m == 3 and g(i, 0, m):
# #             print("^ OK")
# #             mass.append(i)
# #
# # print(len(mass))
#
#         if g(i, 0, m):
#             if m == 2 or m == 4:
#                 print(i, m)
#                 g(i, 0, m, print_move=True)
#                 print('===============')
'''
19.  34
20.  24 -  1+
21.  11 34 + -  11+ 32+
'''

'19.49'
# def g(a, b, c, m):
#
#     # print('\t' * c, a, b, '\t', ("" if not(a+b <= 20) else ("V" if c % 2 == m % 2 else "X")))
#
#     if a + b <= 20:
#         return c % 2 == m % 2
#     if c == m:
#         return 0
#
#     h = [g(a-1, b, c+1, m), g(a, b-1, c+1, m),
#         g((a+1)//2, b, c+1, m), g(a, (b+1)//2, c+1, m)]
#
#
#     return any(h) if (c+1)%2 == m%2 else all(h)
#
#
# for n in range(11, 100):
#     for m in range(6):
#         # if g(10, n, 0, m) and m == 2:
#         #     print(n, m)
#         # if g(10, n, 0, m) and m == 3:
#         #     print(n, m)
#         if m == 4 and g(10, n, 0, m):
#             print(n, m, '=======================')
'''
19.  21 +
20.  22 42 + +
21.  - 24+
'''

'19.71'
# def f(a, b, c, m):
#     print('\t' * c, a, b, '\t', ("" if not (a + b > 68) else ("V" if c % 2 == m % 2 else "X")))
#     if a + b > 68:
#         return c%2 == m%2
#     if c == m:
#         return 0
#
#     h = [f(a+1, b, c+1, m), f(a, b+1, c+1, m), f(a+b, b, c+1, m), f(a, b+a, c+1, m)]
#
#     return any(h) if (c+1)%2 == m%2 else all(h)
#
#
# for n in range(1, 60):
#     for m in range(1, 5):
#         # if f(8, n, 0, m) and m == 2:
#         #     print(n, m)
#         # if f(8, n, 0, m) and m == 3:
#         #
#         #     print(n, m)
#         #     print('================')
#         if f(8, n, 0, m) and m == 4:
#             print(n, m)
#             print('================')
# '''
# 19.  30 -  18?
# 20.  22 29 - +  x? 29
# 21.  30
# '''


'19-21 статград'
# from functools import *
#
# win_sum = 46
#
#
# def next_moves(c):  # c = (a, b)
#     if c[0] > c[1]:
#         return [(c[0], c[1] + i) for i in range(1, c[1] + 1)]
#     elif c[0] < c[1]:
#         return [(c[0] + i, c[1]) for i in range(1, c[0] + 1)]
#     else:
#         return [(c[0], c[1] + i) for i in range(1, c[1] + 1)] + [(c[0] + i, c[1]) for i in range(1, c[0] + 1)]
#
#
# @lru_cache(None)
# def game(c):
#     if c[0] + c[1] >= win_sum:
#         return '+'
#     # за один ход (какой-то) достижима победная позиция -- победа Пети первым ходом
#     if any(game(m) == '+' for m in next_moves(c)):
#         return 'P1'
#     # за один ход (каждый) достижима позиция, откуда есть выигр.стр. за один ход -- победа Вани первым ходом (при каждом первом ходе Пети)
#     if all(game(m) == 'P1' for m in next_moves(c)):
#         return 'V1'
#     # за один ход (какой-то) достижима позиция, откуда есть выигр.стр. след. ходом -- победа Пети вторым ходом
#     if any(game(m) == 'V1' for m in next_moves(c)):
#         return 'P2'
#     # за один ход (какой-то) достижима позиция, откуда есть выигр.стр. за 1 ИЛИ 2 хода -- победа Вани первым/вторым ходом
#     if all(game(m) == 'P1' or game(m) == 'P2' for m in next_moves(c)):
#         return 'V2'
#     # в остальных случаях по умолчанию возвращается None -- победа достижима минимум третьим ходом
#
#
# min_sum = 999999
#
# # for f in range(1, 46):
# #     for s in range(f, 46):
# #         if game((f, s)) == 'P1':
# #             min_sum = min(min_sum, f+s)
# #             print(f + s, game((f, s)))
# #
# # print(min_sum)
#
#
# # maxS = 0
# # minS = 99999
# # for s in range(1, 41):
# #     if game((5,s)) == 'P2':
# #         maxS = max(maxS, s)
# #         minS = min(minS, s)
# #
# # print(minS, maxS)
#
#
# minS = 9999
# for s in range(1, 41):
#     if game((5, s)) == 'V2':
#         minS = min(minS, s)
#
# print(minS)
#
# '''
# 19 - 31
# 20 - 24 33
# 21 - 20
#
# '''


'19-21 статград'
from functools import *

def next_moves(c):
    if c[0] < c[1]:
        return [(c[0], c[1] + i) for i in range(1, 4)] + [(c[0] * 2, c[1])]

    elif c[0] > c[1]:
        return [(c[0] + i, c[1]) for i in range(1, 4)] + [(c[0], c[1] * 2)]

    else:
        return [(c[0] + i, c[1]) for i in range(1, 4)] + [(c[0], c[1] + i) for i in range(1, 4)]


@lru_cache(None)
def game(c):
    if sum(c) > 40:
        return 'win'

    if any(game(m) == 'win' for m in next_moves(c)):
        return 'P1'

    if all(game(m) == 'P1' for m in next_moves(c)):
        return 'V1'

    if any(game(m) == 'V1' for m in next_moves(c)):
        return 'P2'

    if all(game(m) == 'P1' or game(m) == 'P2' for m in next_moves(c)):
        return 'V2'




# minS= 9999
# for f in range(1, 41):
#     for s in range(f, 41):
#         if game((f,s)) == 'P1':
#             minS = min(minS, f+s)
#
# print(minS)


# minS = 9999
# maxS = 0
# for s in range(1, 36):
#     if game((5, s)) == 'P2':
#         minS = min(minS, s)
#         maxS = max(maxS, s)
#
# print(minS, maxS)


for s in range(1, 24):
    if game((17, s)) == 'V2':
        print(s)


'''
19 - 28 +
20 - 20 29 +
21 - 9 + 
'''


def f(s, c, m):
    if s >= 351:
        return c % 2 == m % 2
    if c == m:
        return 0

    h = [f(s+1, c+1, m), f(s+4, c+1, m), f(s*2, c+1, m)]

    return any(h) if (c + 1) % 2 == m % 2 else all(h)

print(f'19 {[s for s in range(1, 351) if f(s, 0 , 2)]}')

print(f'20 {[s for s in range(1, 351) if f(s, 0, 3) and not(f(s, 0, 1))]}')

print(f'21 {[s for s in range(1, 351) if (f(s, 0, 2) or f(s, 0, 4)) and not(f(s, 0, 2))]}')