'Задача 12'
#
# s = '8' * 70
# while '8888' in s or '2222' in s:
#     if '2222' in s:
#         s = s.replace('2222', '88', 1)
#     else:
#         s = s.replace('8888', '22', 1)
#
# print(s)


'Задача 12.242'
# import re
#
# s = '>' + '1'*25 + '2'*17 +  '3'*10
# ns = []
#
# while '>1' in s or '>2' in s or'>3' in s:
#     if re.search('>1', s):
#         s = re.sub('>1', '22>3', s, 1)
#
#     if re.search('>2', s):
#         s = re.sub('>2', '2>', s, 1)
#
#     if re.search('>3', s):
#         s = re.sub('>3', '11>2', s, 1)
#
# print(sum(map(int, re.split(r'\D?',s)[1:-2])))

# Ответ: 274


'Задача 12 статград'
# from itertools import *
#
# for c in combinations(range(20), 10):
#     k = ['2'] * 20
#     for i in c:
#         k[i] = '1'
#     s = '0' + ''.join(k) + '0'
#
#     while not '00' in s:
#         s = s.replace('012', '30', 1)
#         if '011' in s:
#             s = s.replace('011', '20', 1)
#             s = s.replace('022', '40', 1)
#         else:
#             s = s.replace('01', '10', 1)
#             s = s.replace('02', '101', 1)
#
#
#     if s.count('1') == 7 and s.count('2') == 5:
#         print(s.count('3'))


'Задача 12 статград'
# from itertools import *
# min4 = 99999999
# for i in range(2, 21, 2):
#     for c in combinations(range(i), i//2):
#         k = ['2'] * i
#         for l in c:
#             k[l] = '1'
#         s = '0' + ''.join(k) + '0'
#
#         while not '00' in s:
#             if '011' in s:
#                 s = s.replace('011', '101', 1)
#             else:
#                 s = s.replace('01', '40', 1)
#                 s = s.replace('02', '20', 1)
#                 s = s.replace('0222', '1401', 1)
#
#         if s.count('1') == 6 and s.count('2') == 9:
#             min4 = min(min4, s.count('4'))
#
#         print(min4)


'Задача 12 статград'
# from itertools import combinations
#
#
# ran = 6
#
# for n in combinations(range(ran), r=ran//2):
#     # print(n)
#     l = ['1'] * ran
#     for m in n:
#         l[m] = '2'
#
#     s = '0'+ ''.join(l) +'0'
#     print(s, end='\t')
#     while '00' not in s:
#         s = s.replace('02', '101', 1)
#         s = s.replace('11', '2', 1)
#         s = s.replace('12', '21', 1)
#         s = s.replace('010', '00', 1)
#     print(s)

# i = 0
# k = 2
# for n in range(2, 149+4, 2):
#     i+=1
#     if i % 2 == 0:
#         k+=2
#
#     elif i % 2 == 1:
#         k += 1
#
#     print(n, k)


'Задача 12 статград'
# def f(s):
#     while '00' not in s:
#         s =s.replace('02','101',1)
#         s =s.replace('11','2',1)
#         s =s.replace('012','30',1)
#         s =s.replace('010','00',1)
#     return s
#
#
# def sum_digit(n):
#     return sum(map(int, list(n)))
#
#
# def check(n):
#     m = sum_digit(n)
#     for d in range(2, m//2):
#         if m % d == 0:
#             return False
#     else:
#         return True
#
#
# from itertools import *
# for n in range(6, 12):
#     for c in combinations(range(n), r=5):
#         s = '0' + ''.join(('1' if j in c else '2') for j in range(n)) + '0'
#         r = f(s)
#
#         if check(r):
#             # print(s, r, True)
#             print(n, '\t', s, '\t', s.count('2'), '\t', r, '\t', sum_digit(r))
#
#
# for x2 in range(41, 1000):
#     n = 40 + x2*2 -1
#     for d in range(2, n//2+1):
#         if n % d == 0:
#             break
#     else:
#         print(x2)
#         break


'12 школьное'

# for n in range(1, 100):
#     for n1 in range(1, 100):
#         for n2 in range(1, 100):
#             s = '0' + '1'*n +'2'*n1 + '3'*n2
#             while '01' in s or '02' in s or '03' in s:
#                 s = s.replace('01', '2302', 1)
#                 s = s.replace('02', '10', 1)
#                 s = s.replace('03', '201', 1)
#             if s.count('1') == 40 and s.count('2') == 10 and s.count('3') == 8:
#                 print(n)
#                 break


for i in range(100):
    s = '1'
    s+= '7'*i
    while '17' in s or '377' in s or '777' in s:
        if '17' in s:
            s = s.replace('17', '1', 1)
        if '377' in s:
            s = s.replace('377', '73', 1)
        if '777' in s:
            s = s.replace('777', '3', 1)
    if s.count('3') ==2:
        print(i)
        break
