'Задача 8'

# Определите количество пятизначных чисел, записанных в восьмеричной
# системе счисления, в записи которых только одна цифра 6, при этом никакая
# нечётная цифра не стоит рядом с цифрой 6
# from itertools import *
# import re
# result = 0
# for comb in product('01234567', repeat=5):
#     numb = ''.join(comb)
#     res = re.findall(r'([1357]6)', numb) + re.findall(r'(6[1357])', numb)
#     if numb.count('6') == 1 and res == [] and numb[0] != '0':
#         result +=1
# print(result)
# result = 0
# exCombs = ['16', '36', '56', '76', '61', '63', '65', '67']
#

# for a in '1234567':
#     for b in '01234567':
#         for c in '01234567':
#             for d in '01234567':
#                 for e in '01234567':
#                     combs = a+b+c+d+e
#                     if combs.count('6') == 1 and not any(s in combs for s in exCombs):
#                         result +=1
#
# print(result)
# Ответ: 2961

'Задача 8 статград'
# from itertools import product
# c= 0
# for w in product('ВЕРОНИКА',  repeat= 6):
#     word = ''.join(w)
#     word = word.replace('В', '1')
#     word = word.replace('Р', '1')
#     word = word.replace('Н', '1')
#     word = word.replace('К', '1')
#     if word.count('1') < 3:
#         c +=1
#
# print(c)

#90112

'Задача 8 статград'
# from itertools import *
#
# def check(n):
#     if n[2] - n[1] == 1:
#         return False
#     elif n[1] - n[0] == 1:
#         return False
#     return True
#
#
# k =0
# for i in combinations(range(11), 3):
#     i = list(i)
#     if check(i) == True:
#         k+=1
# print(k, k*(4**11))


'задача 8 статград'
# from itertools import product
# c= 0
# execept = ['ИО','ИА','ИИ',
#            'ОИ','ОА','ОО',
#            'АИ','АО','АА']
#
# for word in product('МИТРОФАН',  repeat= 6):
#     if len(set(word)) == 6:
#         w = ''.join(word)
#         sogl = w.count('М') + w.count('Т')+ w.count('Р') + w.count('Ф') + w.count('Н')
#         glas = w.count('И') + w.count('О') + w.count('А')
#         if sogl > glas:
#             for i in range(len(execept)):
#                 if execept[i] in w:
#                     break
#             else:
#                 c+=1
#
# print(c)



# from itertools import *
# c = 0
# for w in product('АВГДИНОР', repeat=4):
#     c+=1
#     word = ''.join(w)
#     if word[:2] == 'ГО':
#         print(c)
#         break


from itertools import *
a= []
for w in permutations('ВИКТОР'):
    word = ''.join(w)
    a.append(word)
print((sorted(a))[265])


