'Задача 14'


# b = 15
# y = []
# d = {i:str(i) for i in range(10)} | {10:'a', 11:'b', 12:'c', 13:'d', 14:'e'}
# print(d)
# x = int(input('input number in base 10: '))
# while x > 0:
#     y = [d[x % b]] + y
#     x = x // b
#
# print(''.join(y))

# for x in range(15):
#     a = int(f'123{d[x]}5', 15)
#     b = int(f'1{d[x]}233', 15)
#     if (a + b) % 14 == 0:
#         res = (a + b) // 14
#         print(res)
#         break

# for x in range(15):
#     a = 1*15**4 + 2*15**3 + 3*15**2 + x*15**1 + 5*15**0
#     b = 1*15**4 + x*15**3 + 2*15**2 + 3*15**1 + 3*15**0
#     if (a + b) % 14 == 0:
#         res = (a + b) // 14
#         print(res, x)
#         break

# Ответ: 8767

# y = 0
# x = 49**7 + 7**21 - 7
# while x > 0:
#     d = x % 7
#     if  d == 6:
#         y +=1
#
#     x = x // 7
# print(y)

# res = 0
# n = 15*1728**8 + 9*144**12 + 7*12**12 + 154
# while n > 0:
#     f = n % 12
#     if f == 0:
#         res +=1
#     n = n // 12
# print(res)


'задача 14'
# for x in range(37):
#     n = (x + 3*37 + 2*37**2 + 1*37**3) + (9 + 5*37 + x*37**2 + 4*37**3)
#     if n % 36 == 0:
#         print(x, n // 36)


'Задача 14 Статград'

for p in range(10, 100):
    for x in range(p):
        for y in range(p):
            if x == y:
                continue
            #print(int(f'32{x}8', p) + int(f'{x}{x}{x}9', p), int(f'{y}{y}02', p))
            if (8 + x*p + 2*p**2 + 3*p**3) + (9 + x*p + x*p**2 + x*p**3) == (2 + y*p**2 + y*p**3):
                print(x + y*p + y*p**2)
                break


