'Задача 25'
# res = []
# n = 0
# for x in range(1003):
#     val = '121394'
#     if x >= 0 and x < 1000:
#         valMask = val[:5] + str(x) +'4'
#     if x == 1000:
#         valMask = val[:5] + '4'
#     if x == 1001:
#         valMask = val[:5] + '004'
#     if x == 1002:
#         valMask = val[:5] + '0004'
#
#     for y in range(10):
#         valNew = valMask[:1] + str(y) +valMask[1:]
#         if int(valNew) % 2023 == 0:
#             n+=1
#             res.append((int(valNew), int(valNew)//2023))
#
# for p in sorted(res):
#     print(*p)

# res = []
# for y in range(10):
#     for x in list(range(1000)) + ['', '00', '000']:
#         n = int(f'1{y}2139{x}4')
#         if n % 2023 == 0:
#             res.append((n, n//2023))
#
# for p in sorted(res):
#     print(*p)

# # %)
# print()
# for p in sorted([(int(f'1{y}2139{x}4'), int(f'1{y}2139{x}4')//2023) for x in list(range(1000)) + ['', '00', '000'] for y in range(10) if int(f'1{y}2139{x}4') % 2023 == 0]):
#     print(*p)


'Задача 25.21'
# result=[]
# for i in range(452022, 700000):
#     s = 0
#     for k in range(2, i):
#         if i % k == 0:
#             s = k + i//k
#             break
#     if s % 7 == 3:
#         result.append((i, s))
#     if len(result) == 5:
#         for p in sorted(result):
#             print(*p)
#         break
# # Ответ: 452025 150678
# #        452029 23810
# #        452034 226019
# #        452048 226026
# #        452062 226033


'Задача 25 статград'
# 10 000 000 000
# 1? 493 *** -41

# res = []
# for j in range(10):
#     for i in list(range(1000)) + [''] + ['00'] + ['000']:
#         num = int(f'1{j}493{i}41')
#         if num % 2023 == 0:
#             res.append(num)
#
#
#
# print(*sorted(res))

'Задача 25'
# count = 0
# for n in range(174457, 174506):
#     n1 = n
#     i = 2
#     sep = []
#     while n > 1:
#         if n % i == 0:
#             n //=i
#             sep.append(i)
#         else:
#             i+=1
#             if i > n:
#                 break
#
#     if len(set(sep)) == 2:
#         print(n1, set(sep))
#         count +=1
#
# print(count)


# Ответ:
# 174459 {58153, 3}
# 174461 {24923, 7}
# 174463 {59, 2957}
# 174473 {13, 13421}
# 174479 {1171, 149}
# 174483 {3, 19387}
# 174485 {34897, 5}
# 174497 {827, 211}
# 174502 {2, 87251}


'25'
# def div(x):
#     d = set()
#     for i in range(1, int(x**0.5)+1):
#         if x % i ==0:
#             d.add(i)
#             d.add(x//i)
#         return sorted(d)
#
# for x in range(190201, 190281):
#     d = [i for i in div(x) if i%2==0]
#     if len(d) == 4:
#         print(d)


'Задача 25'
# from fnmatch import *
#
# for i in range(0, 10**10, 4891):
#     n = str(i)
#     if fnmatch(n, '1?7602*0'):
#         print(n)


'Задача 25.299'
# from fnmatch import *
# from tqdm import tqdm
#
# for n in tqdm(range(0, 10**11, 279)):
#     x = str(n)
#     if fnmatch(x, '78?56*321'):
#         print(x)

# from itertools import *
#
# mass = []
# for x in range(10):
#     for i in range(1, 4):
#         for l in product('13579', repeat=i):
#             y = ''.join(l)
#             n = int(f'78{x}56{y}321')
#             if n % 279 == 0:
#                 mass.append((n, n // 279))
#
# for x in sorted(mass):
#     print(*x)

'Задача 25.198'
# def div(n):
#     m = []
#     for x in range(2, n//2+1):
#         if n % x == 0 and x % 2 == 0:
#             m.append(x)
#     if len(m) < 5:
#         return [0, 0, 0, 0, 0]
#
#     return m
#
# mass = []
# for i in range(100000000-2, 1, -2):
#     if div(i)[-5] != 0:
#         mass.append((div(i)[-5], len(div(i))))
#     if len(mass) == 5:
#         break
# for x in mass: #sorted(mass, key=lambda p: p[1]):
#     print(*x)



from fnmatch import *

def div(a):
    count = []
    while a > 1:
        for n in range(2, (a//2)+1):
            while a % n == 0:
                count.append(n)
                a //= n
            if a == 1:
                break
    return count

for i in range((10**4)+1):
    n = str(i)
    if fnmatch(n, '*2?2'):
        if len(div(int(n))) == 7:
            print(n, div(int(n)))


def is_prime(n):
    if n % 2 == 0:
        return n == 2

    for a in range(3, int((n**0.5)+1), 2):
        if n % a == 0:
            return 0
    return 1


