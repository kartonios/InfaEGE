# line = open(r"C:\Users\karton\Desktop\EGE\ege\stat202212_files\26.txt").read().splitlines()
# mass_a = []
# mass_b = []
# for x in line:
#     a, type = x.split()
#     a = int(a)
#     if type=='A':
#         mass_a.append(a)
#     else:
#         mass_b.append(a)
#
# mass_a.sort(reverse=True)
# mass_b.sort(reverse=True)
#
# type = 'B'
# block = []
# all_blocks = []
# while mass_a and mass_b:
#     if type == 'B':
#
#         for i in range(len(mass_b)):
#             if block == [] or block[-1] - mass_b[i] >= 7:
#                 block.append(mass_b.pop(i))
#                 type = 'A'
#                 break
#         else:
#             all_blocks.append(len(block))
#             type = 'A' if mass_a[0] > mass_b[0] else 'B'
#             block = []
#
#     else:
#         for j in range(len(mass_a)):
#             if block == [] or block[-1] - mass_a[j] >= 7:
#                 block.append(mass_a.pop(j))
#                 type = 'B'
#                 break
#         else:
#             all_blocks.append(len(block))
#             type = 'A' if mass_a[0] > mass_b[0] else 'B'
#             block = []
#
#
# print(mass_a)
# print(max(all_blocks), len(all_blocks) + len(mass_a))


'Задача 26 Статград'
# from collections import defaultdict
# s = open(r"C:\Users\karton\Desktop\26.txt").read().splitlines()
# s.pop(0)
# # dots = dict()
# dots = defaultdict(set)
# for i in range(len(s)):
#     x, y = map(int, s[i].split())
#     dots[x].add(y)
#     # if x in dots:
#     #     dots[x].append(y)
#     # else:
#     #     dots[x] = [y]
#
#
# dotsCount = 1
# maxLinesInRow = 0
# for x in dots.keys():
#     maxDots = []
#     if len(dots[x]) > 1:
#         ys = sorted(dots[x])
#         for i in range(len(ys)-1):
#             if ys[i+1] - ys[i] == 1:
#                 dotsCount+=1
#             else:
#                 if dotsCount >= 3:
#                     maxDots.append(dotsCount)
#                     dotsCount = 1
#         '''
#                 проблема последней серии
#                 если дошли до края и линия имеет длину более 3
#         '''
#         if dotsCount >= 3:
#             maxDots.append(dotsCount)
#             dotsCount = 1
#
#     if len(maxDots) >= maxLinesInRow:
#         maxLinesInRow = len(maxDots)
#         print(maxLinesInRow, x)


'Задача с массивами'
n = int(input())
A = [[0]*(2*n+1) for i in range(2*n+1)]

def step(a, s, n):
    k = a[n+1][n+1]
    if s % 2 == 1:
        for i in range(1, s):
            a[n+1][n+i] = a[n+1][n+i-1] + 1
        for j in range(1, s):
            a[n-j][n+1] = a[n-j+1][n+1] + 1
        return a
    else:
        for i in range(1, s):
            a[n+1][n-i] = a[n+1][n-i+1] + 1
        for j in range(1, s):
            a[n+j][n+1] = a[n+j-1][n+1] + 1
        return a

S = 0
while A[0][2*n] == 0:
    S+=1
    step(A, S, n)

    for row in A:
        for x in row:
            print(f'{x:3}', end='')
        print()


