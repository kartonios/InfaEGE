'Статград'
'1'
'Ответ 48'

'2'
# print('w x y z')
# for w in range(2):
#     for x in range(2):
#         for y in range(2):
#             for z in range(2):
#                 if (not x or (y == w)) and (y == (not w or z)):
#                     #print('f == 1')
#                     print(w,x,y,z)
#                 # else:
#                 #     print('f == 0')
#                 #     print(w, x, y, z)

'Ответ yxwz'

'3'
'Ответ 7 665 524'


'4'
'Ответ 19'


'5'
# for n in range(10000):
#     r = bin(n)[2:]
#     m = ''
#     for i in range(len(r)):
#         if r[i] == '1':
#             m += '0'
#         else:
#             m+= '1'
#
#     m = str(int(m, 10))
#     if n - int(m, 2) == 999:
#         print(n)
#         break
'Ответ 1011'

'6'


'7'
'Ответ 24'


'8'
# res = 0
# mass = []
# for i in range(100000, 10000000):
#     n = ''
#     m = 0
#     while i > 0:
#         n = str(i % 9) + n
#         i //= 9
#
#     for j in range(len(n)):
#
#         if int(n[j], 10) % 2 == 1:
#             m+=1
#
#     if n.count('6') == 1 and m == 2 and len(n) == 7:
#         mass.append(n)
#         res += 1
#
#
# print(mass, res)
'Ответ 368640'


'9'
# from collections import *
#
# def diff(N):
#     val = list(set(N))
#     if len(val) != 4:
#         return [0, 0]
#     res = 0
#     num = []
#     for i in range(len(val)):
#         if N.count(val[i]) == 2:
#             res+=1
#             num.append(val[i])
#     if res == 2:
#         return num
#     else:
#         return [0, 0]
#
#
# def check(n):
#     val = list(set(n))
#     if len(val) != 4:
#         return False
#
#     a = Counter(n)
#     s = 0
#     if sorted(a.values()) == [1,1,2,2]:
#         for number, repeats in a.items():
#             if repeats == 1:
#                 s += number
#             else:
#                 s -= number
#         if s > 0:
#             return True
#         else:
#             return False
#
#
#
#
#
# s = open(r"D:\downloads\ggg\09F.txt").read().splitlines()
# l = []
# k = []
# for line in s:
#     l.append(list(map(int, line.split())))
#
#
# # for p in range(len(s)):
# #     k.append(int(s[p], 10))
# #     if len(k) == 6:
# #         l.append(k)
# #         k = []
#
#
#
#
# result = 0
# for line in l:
#     if check(line):
#         result += 1
#
# # for i in range(len(l)):
# #     d = sum(diff(l[i]))
# #     if len(set(l[i])) == 4 and d > -1:
# #         if sum(set(l[i])) > d:
# #             result+=1
#
# print(result)
'Ответ 351'


'10'
'Ответ 7'


'11'
'Ответ 14'

'12'
# from itertools import *
# from tqdm import *
# for i in range(1, 300):
#     for c in tqdm(product('12', repeat=i*2)):
#         s = ''.join(c)
#         if s.count('1') != s.count('2'):
#             continue
#         line = f'0{s}0'
#         while line.count('00') != 1:
#             line = line.replace('011','20', 1)
#             line = line.replace('022', '10', 1)
#             line = line.replace('01', '220', 1)
#             line = line.replace('02', '110', 1)
#
#         if line.count('1') == 40 and line.count('2') > 50:
#             print(line.count('2'), i,  '0' + '1'*i + '2'*i +'0')
#             break
#
# for i in range(10, 100):
#     for j in range(10, 100):
#         line = '0' + '1'*i + '2'*j + '0'
#         while line.count('00') != 1:
#             line = line.replace('011','20', 1)
#             line = line.replace('022', '10', 1)
#             line = line.replace('01', '220', 1)
#             line = line.replace('02', '110', 1)
#
#         if line.count('1') == 40 and line.count('2') > 50 and i == j:
#             print(line.count('2'))
#             break

'============================================================================='

'13'



'14'
# for x in list(range(10)) + ['A'] + ['B'] + ['C'] + ['D'] + ['E'] + ['F']:
#     l = int(f'1{x}BAD', 16) + int(f'2C{x}FE', 16)
#     if l % 15 == 0:
#         print(l//15)
#         break

# Ответ: 18341


'15'
# def f(n, m):
#     return n % m == 0
#
#
# for A in range(1, 1000):
#     for x in range(1, 1000):
#         if ((not f(72, x) or not f(120, x)) or (A - x > 100)) == False:
#             break
#     else:
#         print(A)
#         break
# # Ответ: 125

'16'
# from tqdm import *
# def f(n):
#     return ((1 + n) * n) // 2 # Арифметическая прогрессия
#
#
# res =[]
# lower = 237567892
# upper = 1134567004
# for N in list(range(lower, lower+10)) + list(range(upper, upper+10)):
#     num = f(N)
#     print(N, num, num % 3, sep='\t')
#
#
# print(res)   #298 999 706
#
# # 6 7 8 9 10 11 12
# # 1 0 0 1 0  0  1
# # (12 - 6) / 3 = 6/3 = 2     + 1 !!!
# print((upper - lower)//3 + 1)

'17'
# line = open(r"D:\downloads\ggg\17.txt").read().split()
# minN = 9999999
# pairs = 0
# maxPair = 0
#
#
# for i in line:
#     if abs(int(i)) % 10 == 7 and '-' in i:
#         minN = min(minN, int(i))
#
#
# for i in range(len(line)-1):
#     f = abs(int(line[i]))
#     s = abs(int(line[i+1]))
#     if ((f % 10 == 7) != (s % 10 == 7)) and f**2 + s**2 < minN**2:
#         pairs+=1
#         maxPair = max(maxPair, f**2 + s**2)
#
# print(pairs, maxPair)
#
# # Ответ: 671 96731834

'18'

'19'

'20'

'21'

'22'

'23'
# Ответ 16

'24'
# Ответ 5

'25'
# res = []
# for i in range(10):
#     for j in list(range(1000)) + [''] + ['00'] + ['000']:
#         num = int(f'1{i}493{j}41')
#         if num % 2023 == 0:
#             res.append(num)
#
# print(sorted(res))
# # Ответ [1349341, 1249338041, 1549348941, 1849359841]


'26'
# l = list(map(int, open(r"D:\downloads\ggg\26.txt").read().split()))
# n = l.pop(0)
# l = sorted(l, reverse=True)
# print(l)
#
#
#
#
# def localMax(L):
#     lm = 0
#     for i in L:
#         lm = max(lm, i)
#     return lm
#
#
# def put(line):
#     lMax = localMax(line)
#     line.remove(lMax)
#     box = 1
#     i = 0
#     while i < len(l):
#         if lMax - l[i] >= 5:
#             box +=1
#             lMax = l[i]
#             line.remove(l[i])
#         else:
#             i += 1
#     return box
#
# # 5
# # 20
# # 3
# # 7
# # 1
# # 8
#
# # 1 3 7 8 20
#
# storage = []
# while len(l) > 0:
#     storage.append(put(l))
#
# print(len(storage), sorted(storage, reverse=True))
# # Ответ 1696



'26 demo'
# l = list(map(int, open(r"C:\Users\karton\Desktop\EGE\demo2023_files\Задание 26\26.txt").read().split()))
# l = sorted(l, reverse=True)
# trash = l.pop(0)
# present = []
#
# def LM(n):
#     maxN = 0
#     for i in n:
#         maxN = max(maxN, i)
#     return maxN
#
#
# def put(L):
#     maxN = LM(L)
#     box = []
#     box.append(maxN)
#     i = 0
#     while i < len(l):
#         if maxN - L[i] >= 3:
#             box.append(L[i])
#             maxN = L[i]
#             l.remove(L[i])
#         else:
#             i+=1
#     return box
#
#
# present = put(l)
# print(len(present), min(present))
# #Ответ 2767 51

#
# def f(s, n):
#     if s > n:
#         return 0
#     if s == n:
#         return 1
#
#     res = f(s, n-1)  # +1
#     if n % 3 == 0:
#         res += f(s, n // 3)
#     if n % 2 == 0:
#         res += f(s, n // 2)
#     return res
#
#
# print(f(2, 20))

'23 demo'
# def f(s, n):
#     if s > n or n == 17:
#         return 0
#     if s == n:
#         return 1
#
#     res = f(s, n-1)
#     if n % 2 == 0:
#         res += f(s, n//2)
#     return res
#
#
# print(f(1, 10)*f(10, 35))


'23 statgrad'
# def f(s, n):
#     if s > n or '3' in str(n):
#         return 0
#     if s == n:
#         return 1
#
#     res = f(s, n-1)
#     if n % 2 == 0:
#         res += f(s, n//2)
#     return res
#
#
# print(f(1, 40))


'Задача 9'
def f(s, n):
    if s > n:
        return 0
    if s == n:
        return 1

    res = f(s, n-3)
    if n % 2 == 0:
        res += f(s, n-2) + f(s, n-1)

    return res


print(f(1, 18))

'22 demo-statgrad'
# s = open(r"D:\downloads\ggg\asdasd.txt").read().splitlines()
# t = dict()
# p = dict()
# for l in s:
#     id, time, parents = l.split('\t')
#     t[id] = int(time)
#     p[id] = parents.split(';')
#
# print(t, p)
#
# def count_time(id):
#     if p[id] == ['']:
#         return t[id]
#     else:
#         max_t = 0
#         for parent in p[id]:
#             max_t = max(max_t, count_time(parent))
#         return max_t + t[id] + 3 # +3 мс задержки, по условию задачи
#
#
# res = []
# for id in t.keys():
#     res.append(count_time(id))
#     print(id, count_time(id))
#
# print(max(res))

