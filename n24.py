'Задача 24'
# read() учитывает \n в файле
# s = open(r"C:\Users\karton\Desktop\EGE\demo2023_files\Задание 24\24.txt").read()
# for i in range(len(s)-1):
#     s[i:i+2] == 'BA'
# print(s[:10])
# print('------')


'Задача 24.91'
# s = open(r"C:\Users\karton\Desktop\EGE\24-1.txt").read()
#
# m = []
# xs = ''
# for i in range(len(s)):
#     if s[i] in '13579':
#         xs += s[i]
#     else:
#         if xs != '':
#             m.append(int(xs))
#         xs = ''
#
# print(m)


'Задача 24.148'
# from collections import Counter
#
# s = open(r"C:\Users\karton\Desktop\EGE\24-s2.txt").read()
# n = ''
# for i in range(len(s)-1):
#     if s[i].find('X') == False:
#         n = n + s[i+1:i+2]
#
# print(Counter(n).most_common())  #Ответ: U1618


'Задача 24.91'
# from collections import Counter
#
# lines = open(r"C:\Users\karton\Desktop\EGE\s202103_24.txt").read().splitlines()
# min_g = 9999999999999999999999
# min_s = ''
# for s in lines:
#     if s.count('G') < min_g:
#         min_g = s.count('G')
#         min_s = s
#
# print(Counter(min_s).most_common())  #Ответ: T


'Задача 24.130'
# s = list(open(r"C:\Users\karton\Desktop\EGE\24-5.txt").read())
# res = 0
#
# for i in range(len(s)):
#     if s[i] == ')':
#         s[i] = '('
#         res += 1
#     if res == 9999:
#         break
#
# print(s.index(')')+1) #Ответ: 19856


'Задача 24.166'
# s = list(open(r"C:\Users\karton\Desktop\EGE\24\24-164.txt").read().splitlines())
# res = []
# maxGap = 1
# for line in s:
#     if line.count('G') < 15:
#         # print(line[2:2+4].rfind('C'))
#         letters = set(line)
#         for c in letters:
#             first = line.find(c)
#             last = line.rfind(c)
#             if last - first > maxGap:
#                 maxGap = last - first
#
#         # for k in range(0, len(line)):
#         #     if line[k+maxGap:].rfind(line[k]) - line[k:].find(line[k]) > maxGap:
#         #         maxGap = line[k+maxGap:].rfind(line[k]) - line[k:].find(line[k])
#
# print(maxGap)
# # Ответ: 156


'Задача 24.165'
# s = list(open(r"C:\Users\karton\Desktop\EGE\24\24-164.txt").read().splitlines())
# alfb = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
# mg = 2
# letter = ''
# res = 0
# for line in s:
#     for i in alfb:
#         let = i*mg
#         if line.find(let) > 0:
#             mg+=1
#             letter = let
#
# for line in s:
#    res += line.count(letter[:1])
#
# print(letter[:1], res)

# Ответ: X36370


'Задача 24.179'
# from collections import Counter
# import re
# res = []
# s = open(r'C:\Users\karton\Desktop\EGE\24\24-179.txt').read()
# for m in re.findall(r'(?=(CB[CDE]BC))', s):
#     res.append(m[2])
#
#
# print(Counter(res).most_common(), sum(Counter(res).values()))

# from itertools import *
# for c in product('abc', repeat=3):
#     print(''.join(c))



'Задача 24 статград'
# import re
# s = open(r"C:\Users\karton\Desktop\EGE\24\24stat.txt").read()
# res = []
# for m in re.finditer(r'([CDF][CDF][AO])+', s):
#     res.append(m[0])
#
# maxL = len(max(res, key=len))
#
# print(maxL // 3, max(res, key=len))


'Задача 24 статград'
# import re
# line = open(r"C:\Users\karton\Desktop\EGE\ege\stat202212_files\24.txt").read()
# #line = 'FAKAJSFFFF'
# #line = 'FAAFABAFAAACCCCCFAFBBBF'
# # lenl = 0
# # flag = False
# # countA = 0
# # all_lens = []
# # max_lenl = 0
# # for j in range(len(line)):
# #     i = line[j]
# #     if i == 'F' and flag == False:
# #         lenl +=1
# #         flag = True
# #
# #     elif i == 'F' and flag == True:
# #         lenl +=1
# #         if countA <= 2:
# #             if lenl > max_lenl:
# #                 max_lenl = lenl
# #                 print(lenl, j, line[j-lenl+1:j+1])
# #
# #     elif i == 'A':
# #         countA +=1
# #         lenl+=1
# #         if countA > 2:
# #             flag = False
# #             countA = 0
# #             lenl = 0
# #
# #     elif flag == True and countA < 3:
# #         lenl+=1
# #
# #
# #
# # print(max_lenl)
# maxlen = 0
# for m in re.finditer(r'(F[CDO]*A?[CDO]*A?[CDO]*)+F',line):
#     maxlen = max(maxlen, len(m[0]))
#     print(maxlen)
#     # 266
l = open(r"C:\Users\karton\Desktop\2412.txt").read().splitlines()
alfb = 'QWERTYUIOPASDFGHJKLZXCVBNM'
maxAlfb =0
for i, s in enumerate(l):
    for c in alfb:
        for k in range(1, len(s)):
            if c*k in s:
                if k >= maxAlfb:
                    maxAlfb = k
                    charCount = s.count(c)
                    print(i, c, k, maxAlfb, charCount)
            else:
                break



