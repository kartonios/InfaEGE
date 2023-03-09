'Комбинаторика Stepik'
'1.8 Задача 9'
# from itertools import *
# res = 0
# for k in product('СКРИПТЫ', repeat=4):
#     word = ''.join(k)
#     if word.count('И') == 1 and word.count('Ы') == 0:
#         res +=1
#     if word.count('Ы') == 1 and word.count('И') == 0:
#         res += 1
# print(res)
# Ответ: 1000


'1.8 Задача 10'
# from itertools import *
# res = 0
# for i in product('АЛГОРИТМ', repeat=3):
#     word = ''.join(i)
#     if word.count('А') > 0:
#         res +=1
#     elif word.count('О') > 0:
#         res +=1
#     elif word.count('И') > 0:
#         res +=1
# print(res)
# #Ответ: 387


'1.8. Задача 11'
# from itertools import *
# res = 0
# exWord = 0
# for f in product('ФУНКЦИЯ', repeat=4):
#     word=''.join(f)
#     if word[0] in 'ФНКЦ':
#         res += 1
#         for j in range(len(word)-1):
#             if word[j] == word[j+1]:
#                 exWord += 1
#                 break
#
# print(res-exWord)
# # Ответ: 864

'1.9 Задача 1'
# from itertools import *
# res = 0
# for w in product('СТРМ', repeat=5):  # Буква 'И' никак не задействована, поэтому ее можно исключить из алфавита
#     word = ''.join(w)
#     if word[0] == word[4] and word [1] == word[3]:
#         res +=1
#
# print(res)
# #Ответ: 64


'1.9 Задача 2'
# from itertools import *
# res = 0
# for w in product('ЭКРАН', repeat=5):
#     word = ''.join(w)
#     if word.count('А') >= 2:
#         res +=1
#
# print(res)
# # Ответ: 821


'1.9 Задача 3'
# from itertools import *
# res = 0
#
# for p in product('ПАРОЛЬ', repeat=6):
#     password = ''.join(p)
#     if len(set(password)) == 6 and not 'ОЬА' in password and not 'АЬО' in password:
#         res +=1
#
# print(res)
# # Ответ: 672


'1.9 Задача 4'
# from itertools import *
# res = 0
# for w in product('ПАРОЛЬ', repeat=6):
#     word = ''.join(w)
#     if len(set(word)) == 6 and word[0] != 'Ь' and not 'АЬ' in word and not 'ОЬ' in word:
#         res +=1
#
# print(res)
# # Ответ: 360


'1.9 Задача 5'
#
# from itertools import *
# res = 0
# for w in product('ПАРОЛЬ', repeat=6):
#     word = ''.join(w)
#     if len(set(word)) == 6 and word[0] != 'Ь' and word[5] != 'Ь' \
#             and not 'АЬ' in word and not 'ОЬ' in word:
#         res +=1
#
# print(res)
# # Ответ: 288


'1.9 Задача 6'
#
# from itertools import *
# res = 0
# for w in product('ДАТЧИК', repeat=6):
#     word = ''.join(w)
#     if len(set(word)) == 6 and word[0] != 'А' and word[0] != 'И' and not 'КД' in word:
#         res +=1
#
# print(res)
# # Ответ: 408


'1.9 Задача 7'
# from itertools import *
# res = 0
# for b in product('ДИСК', repeat=5):
#     word = ''.join(b)
#     if 'Д' in set(word) and 'К' in set(word):
#         res+=1
#
# print(res)
# #Ответ: 781


'1.9. Задача 8'
# from itertools import *
# res = 0
# for m in product('ВЕБСАЙТ', repeat=4):
#     word = ''.join(m)
#     if word[0] != 'Й':
#         if 'Е' in set(word) or 'А' in set(word):
#             res +=1
# print(res)
# # Ответ: 1558


'1.9 Задача 9'
# from itertools import *
# res = 0
# for j in product('ТВИЕР', repeat=7):
#     word = ''.join(j)
#     if word.count('Т') == 3 and word.count('В') == 1 and word.count('И') == 1 and \
#             word.count('Е') == 1 and word.count('Р') == 1:
#         res +=1
# print(res)
# # Ответ: 840


'1.9 Задача 13'
# from itertools import *
# res = 0
# for n in product('0123456789', repeat=4):
#     number = ''.join(n)
#     if number[0] !='0':
#         if len(set(number)) <= 2:
#             res +=1
# print(res)
# # Ответ: 576
# from itertools import *
# import re
# n = int(input()) # кол-во пряностей
# a = input().split() # цены на пряности в первом городе
# b = input().split() # цены на пряности во втором городе
#
# maxP = 0
# s1=1
# s2=1
#
# for i in product(range(10**n + 1), repeat=n):
#     w = []
#     for m in re.findall('\d+', str(i)):
#         w.append(int(m))
#
#     for k in range(n):
#         s1 += w[k]*int(a[k])
#         s2 += (10**n-w[k])*int(b[k])
#
#     if abs(s1 - s2) <= 10**(n+1) and s1 > maxP :
#         maxP = s1/10**n
#     s1 = 0
#     s2 = 0
# print(maxP)



# from itertools import *
# res = []
# for i in product('49', repeat=6):
#     num = int(''.join(i))
#     if num % 13 == 0 and str(num)[0] == '4' and  str(num)[5] == '9':
#         res.append(num)
#
#
# for j in product('450', repeat=6):
#     num = int(''.join(j))
#     if num % 13 == 0 and str(num).count('0') == 3:
#         res.append(num)
#
# print(sorted(res))

'codeforces 1'
n = int(input())
for i in range(n):
    x, y, k = input().split()
    x = int(x)
    y = int(y)
    k = int(k)
    x1 = 1
    y1 = 1
    if (x - x1) * y1 + (y - y1) * x == k:
        print('YES')
    elif:
        print('MB')
    else:
        print('NO')

