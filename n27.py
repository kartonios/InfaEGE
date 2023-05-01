'Задача 27A'
# def config(M, D, i):
#     s = 0
#     for j in range(len(D)):
#         s += abs(D[j] - D[i]) * M[j]
#     return s
#
#
# K = 36
# lines = open(r"C:\Users\karton\Desktop\EGE\demo2023_files\Задание 27\27_A.txt").read().splitlines()
# lines.pop(0)
# mass = []
# dist = []
# for line in lines:
#     d, p = map(int, line.split())
#     if p % K != 0:
#         mass.append(p // K + 1)
#     else:
#         mass.append(p // K)
#     dist.append(d)
#
#
# res = []
# for a in range(len(dist)):
#     res.append(config(mass, dist, a))
#
# print(list(zip(mass, dist)))
# print(min(res))


'Задача 27A'
# def config(M, D, i):
#     s = 0
#     for j in range(len(D)):
#         s += abs(D[j] - D[i]) * M[j]
#     return s
#
#
# K = 36
# lines = open(r"C:\Users\karton\Desktop\EGE\demo2023_files\Задание 27\27_A.txt").read().splitlines()
# lines.pop(0)
# mass = []
# dist = []
# sums = [0]
# for line in lines:
#     d, p = map(int, line.split())
#     if p % K != 0:
#         mass.append(p // K + 1)
#     else:
#         mass.append(p // K)
#     dist.append(d)
#     sums.append(sums[-1] + d)
#
# for a in range(len(dist)):
#     for j in range(len(D)):
#         s += abs(D[j] - D[i]) * M[j]
#
#
# print(list(zip(mass, dist)))
# print(min(res))


'Задача 27B'
# k = 36
# s = open(r"C:\Users\karton\Desktop\EGE\demo2023_files\Задание 27\27_B.txt").read().splitlines()
# n = int(s.pop(0))
# sp = [0]
# t = 0
# min_t = 99999999999999999999999
# dist = []
#
# for i in range(n):
#     d, p = map(int, s[i].split())
#     dist.append(d)
#     if p % k != 0:
#         box = p // k + 1
#     else:
#         box = p // k
#     sp.append(sp[-1] + box)
#     if i > 0:
#         t += box * (dist[-1] - dist[0])
#
# # first option
# for j in range(1, n):
#     s_left = sp[j]
#     s_right = sp[-1] - s_left
#     del_d = dist[j] - dist[j-1]
#     t += del_d * (s_left - s_right)
#     min_t = min(min_t, t)
#
# print(min_t)


'Задача 1'
# n = int(input())
# k = 0
# MaxNegative = -99999999999999
# i_neg = 0
# i0 = 0
#
# for i in range(1, n+1):
#     x = int(input())
#     if x != 0:
#         if x < 0:
#             if MaxNegative < x:
#                 MaxNegative = x
#                 i_neg = i
#             k+=1
#     else:
#         i0 = i
#
# for i in range(1, n+1):
#     if i != i0 and not (i == i_neg and k % 2 != 0):
#         print(i, end=' ')


'Задача 3'
# n = int(input())
# flag = 'pass / fail'
# mass = []
# for i in range(1, n + 1):
#     x = int(input())
#     if x % 5 == 0 or x % 7 == 0:
#         mass.append(x)
#
# mass = sorted(mass, reverse=True)
# multip = int(input())
#
# if multip == 0 and len(mass) == 0:
#     flag = 'pass'
#
# elif multip != 0 and multip % 35 == 0 and len(mass) > 0:
#     remain = multip // mass[0]
#     if remain // mass[1] == 0:
#         flag = 'pass'
#     else:
#         flag = 'fail'
#
# else:
#     flag = 'fail'
#
# if flag == 'fail':
#     for j in range(10):
#         for i in range(j, len(mass) - 1):
#             multip = mass[j] * mass[i+1]
#             if multip % 35 == 0:
#                 break
#         if multip % 35 == 0:
#             break
#     else:
#         multip = 0
#
# print(f'Computed checksum: {multip}')
# print(f'Checksum control: {flag}')

# n = int(input())
# flag = 'pass / fail'
# m5 = 0
# m7 = 0
# m35 = 0
# m = 0
# max_sum = 0
# for i in range(n):
#     k = int(input())
#
#     if k % 35 == 0:
#         m35 = max(m35, k)
#
#     elif k % 7 == 0:
#         m7 = max(m7, k)
#
#     elif k % 5 == 0:
#         m5 = max(m5, k)
#
#     else:
#         m = max(m, k)
#
# control_sum = int(input())
# max_sum = max(m35 * max(m5, m7, m), m5 * m7)
#
# if m5 == 0 and m7 == 0 and m35 == 0:
#     if max_sum == control_sum:
#         flag = 'pass'
#     else:
#         flag = 'fail'
#
# elif max_sum == control_sum:
#     flag = 'pass'
#
# else:
#     flag = 'fail'
#
# print(f'Computed checksum: {max_sum}')
# print(f'Checksum control: {flag}')


'Задача 5'
# n = int(input())
# mass = []
# min3 = 999999999999
# minN = 999999999999
# minRes = 999999999999999999999999
# for i in range(6):
#     mass.append(int(input()))
#
# for i in range(1, n-5):
#     if mass[0] % 3 == 0:
#         min3 = min(min3, mass[0])
#
#     minRes = min(minRes, min3 * mass[5])
#     mass.pop(0)
#     mass.append(int(input()))
#
# if minRes > 10000:
#     minRes = -1
# print(minRes)

'Задача 8.3.10'
# from math import factorial
# n = int(input())
# m = [0, 0, 0, 0, 0, 0, 0, 0]
# pairs = 0
# for i in range(n):
#     N = int(input())
#     if N % 10 == 9:
#         m[0]+=1
#
#     elif N % 10 == 8:
#         m[1]+=1
#
#     elif N % 10 == 7:
#         m[2]+=1
#
#     elif N % 10 == 6:
#         m[3]+=1
#
#     elif N % 10 == 4:
#         m[4]+=1
#
#     elif N % 10 == 3:
#         m[5]+=1
#
#     elif N % 10 == 2:
#         m[6]+=1
#
#     elif N % 10 == 1:
#         m[7]+=1
#
# if m[3] > 0:
#     pairs += factorial(m[3]) // (factorial(m[3]-2) * 2)
# if m[4] > 0:
#     pairs += factorial(m[4]) // (factorial(m[4]-2) * 2)
# pairs += m[0]*m[4] + m[1]*m[6] + m[1]*m[2] + m[3]*m[7] + m[5]*m[6]
#
# print(pairs)


'Задача 8.4.1'
# n = int(input())
# t = [0, 0, 0, 0]
# for i in range(n):
#     x, y = map(int, input().split())
#     if x > 0 and y > 0: # 1 четверть
#         t[0] += 1
#     elif x < 0 and y > 0: # 2 четверть
#         t[1] += 1
#     elif x < 0 and y < 0:
#         t[2] += 1
#     elif x > 0 and y < 0:
#         t[3] += 1
#
# print(t[0] * t[1] + t[1] * t[2] + t[2] * t[3] + t[3] * t[0])


'Задача 27 статград'

# s = list(map(int, open(r"C:\Users\karton\Desktop\EGE\ege\stat202103_files\27\27-A.txt").read().splitlines()))
# ost = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# max_sum = 0
# for x in s:
#     r = x % 3
#     if x > ost[r][0]:
#         ost[r][2] = ost[r][1]
#         ost[r][1] = ost[r][0]
#         ost[r][0] = x
#
#     elif x > ost[r][1]:
#         ost[r][2] = ost[r][1]
#         ost[r][1] = x
#
#     elif x > ost[r][2]:
#         ost[r][2] = x
#
# max_sum = max(max_sum, ost[0][0] + ost[1][0] + ost[2][0])
# for r in range(3):
#     max_sum = max(max_sum, sum(ost[r]))
#
# print(max_sum)
# # Ответ: А - 2697   B - 299986167
# def solve_b(a, control_sum):
#     n = len(a)
#     flag = 'pass / fail'
#     m5 = 0
#     m7 = 0
#     m35 = 0
#     m35_2 = 0
#     m = 0
#     max_sum = 0
#     for i in range(n):
#         k = a[i]
#
#         if k % 35 == 0:
#             m35_2 = m35
#             m35 = max(m35, k)
#
#         elif k % 7 == 0:
#             m7 = max(m7, k)
#
#         elif k % 5 == 0:
#             m5 = max(m5, k)
#
#         else:
#             m = max(m, k)
#
#     max_sum = max(m35 * max(m5, m7, m), m5 * m7, m35 * m35_2)
#
#     if m5 == 0 and m7 == 0:
#         if max_sum == control_sum:
#             flag = 'pass'
#         else:
#             flag = 'fail'
#
#     elif max_sum == control_sum:
#         flag = 'pass'
#
#     else:
#         flag = 'fail'
#
#     return f'Computed checksum: {max_sum}\nChecksum control: {flag}'
#
# def solve_a(a, control_sum):
#     n = len(a)
#     max_sum = 0
#     for i in range(n):
#         for j in range(i+1, n):
#             if a[i]*a[j] % 35 == 0:
#                 max_sum = max(max_sum, a[i]*a[j])
#     if max_sum == control_sum:
#         flag = 'pass'
#     else:
#         flag = 'fail'
#     return f'Computed checksum: {max_sum}\nChecksum control: {flag}'
#
# def check(t):
#     r_a = solve_a(t[:-1], t[-1])
#     r_b = solve_b(t[:-1], t[-1])
#     if r_a == r_b:
#         return 'OK ', t, r_a, r_b
#     else:
#         return 'ERR', t, r_a, r_b
#
# tests = [
#     [77, 35, 201, 7, 25, 100, 7700],
#     [77, 35, 201, 7, 25, 100, 7701],
#     [77, 5, 201, 7, 25, 100, 7700],
#     [77, 5, 201, 7, 25, 100, 7701],
#     [77, 35, 700, 7, 25, 100, 24500],
#     [77, 35, 201, 7, 25, 100, 24501],
#     [44, 11, 2, 22, 27, 3, 0],
#     [44, 11, 2, 22, 125, 3, 0]
#     ]
# for test in tests:
#     print(check(test))

'Задача 8.3.8'
# n = int(input())
# m10 = [0, 0]
# m5 = [0, 0]
# m2 = [0, 0]
# m1 = [0, 0]
#
# for i in range(n):
#     num = int(input())
#     if num % 10 == 0:
#         if num > m10[0]:
#             m10[1] = m10[0]
#             m10[0] = num
#         elif num > m10[1]:
#             m10[1] = num
#
#     elif num % 5 == 0:
#         if num > m5[0]:
#             m5[1] = m5[0]
#             m5[0] = num
#         elif num > m5[1]:
#             m5[1] = num
#
#     elif num % 2 == 0:
#         if num > m2[0]:
#             m2[1] = m2[0]
#             m2[0] = num
#         elif num > m2[1]:
#             m2[1] = num
#
#     else:
#         if num > m1[0]:
#             m1[1] = m1[0]
#             m1[0] = num
#         elif num > m1[1]:
#             m1[1] = num
#
# multip10 = m10[0] * max(m10[1], m2[0])
# multip5 = m5[0] * max(m5[1], m1[0])
# multip2 = m2[0] * m10[0]
# multip1 = m1[1] * m5[0]
# max_multip = max(multip10, multip5, multip2, multip1)
#
# if max_multip > 0:
#     if max_multip % 10 == 0:
#         print(f'{max_multip // m10[0]} {m10[0]}')
#     elif max_multip % 5 == 0:
#         print(f'{max_multip // m5[0]} {m5[0]}')
# else:
#     print(0)

'Задача 8.3.11'
# def combi(N):
#     return (N*(N-1)) // 2
#
#
# n = int(input())
# m = [0 for x in range(10)]
# excep = 0
# for i in range(n):
#     num = int(input())
#     ost = num % 10
#     m[ost] += 1
#
# excep = m[1]*m[9] + m[2]*m[8] + m[3]*m[7] + m[4]*m[6] + combi(m[0]) + combi(m[5])
#
# print(combi(n) - excep)


'27 statgrad'
# l = list(map(int, open(r"D:\downloads\stat202303_files\27-A.txt").read().split()))
# l.pop(0)
# d = {(i, j): 0 for i in range(10) for j in range(10)}
# count = 0
# for n in l:
#     # count+=1
#     n5 = 0
#     n2 = 0
#     while n % 5 == 0:
#         n5+=1
#         n //=5
#
#     while n % 2 == 0:
#         n2 +=1
#         n //= 2
#
#     d[(min(9, n2), min(9, n5))] +=1
#     # if count == 10000:
#     #     break
# pairs = 0
#
# for i, j in d.keys():
#
#     if i < 8 and j < 8:
#         pairs += d[(i, j)] * d[(7-i, 7-j)]
#
#     elif i == 8 and j < 8:
#         for k in range(0, 10):
#             pairs += d[(i, j)] * d[(k, 7 - j)]
#
#     elif i == 9 and j < 8:
#         for k in range(0, 10):
#             pairs += d[(i, j)] * d[(k, 7-j)]
#
#     elif i < 8 and j == 8:
#         for k in range(0, 10):
#             pairs += d[(i, j)] * d[(7-i, k)]
#
#     elif i < 8 and j == 9:
#         for k in range(0, 10):
#             pairs += d[(i, j)] * d[(7-i, k)]
#
#
# print(pairs)
# c= 0
#
# for n in range(10001):
#     for k in range(n+1, 10001):
#         s = str(l[n] * l[k])
#         if s.endswith('0'*7) and not s.endswith('0'*8) and not s.endswith('0'*9):
#             # print(l[n], l[k], l[n]*l[k])
#             c+=1
#
# print(c)


'27 Demo'
from math import *
lines = open(r"C:\Users\karton\Desktop\InfaEGE\demo2023_files\Задание 27\27_A.txt").read().splitlines()
n = lines.pop(0)
dist0, bottles = map(int, lines[0].split())
dist_prev = dist0
box = ceil(bottles / 36)
all_boxes = [0, box]
all_dist = []
total_cost = 0
for l in lines[1:]:
    dist, bottles = map(int, l.split())
    box = ceil(bottles / 36)
    all_boxes.append(box+all_boxes[-1])
    all_dist.append(dist-dist_prev)
    dist_prev = dist
    total_cost += (dist - dist0) * box

print(lines[:10])
print(all_boxes, all_dist)

# min_dist = 99999999999999999999999999999
# c = 0
# for p in range(len(all_boxes)):
#     min_dist = min(min_dist, all_boxes[-1] - all_boxes[-2] + all_boxes[p])
#     # c += all_dist[p]
#     # for i in range(p, len(all_dist)):
#     #     c += all_dist[i] - all_dist[p]
#     print(min_dist)

