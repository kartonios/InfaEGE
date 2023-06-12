'Задача 2'
# print("x y z w")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if not(not(y <= x) or (z <= w) or not z):
#                     print(x, y, z, w)



'Задача 2 Статград'
# print('x y w z')
# for x in range(2):
#     for y in range(2):
#         for w in range(2):
#             for z in range(2):
#                 f1 = (x or not y) <= (w ==z)
#                 f2 = (x or not y) == (z <= w)
#                 # if f1 == 0 and f2 == 0:
#                 #     print(x,y,w,z, 'f1 = 0  f2 = 0')
#                 if f1 == 0:
#                     print(x, y, w, z, 'f1 = 0')
#                 elif f2 == 0:
#                     print(x, y, w, z, '        f2 = 0')
#
#
# # y z x w

print('x y w z')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if (not(x) or (not(y) or not(z))) and y and (not(x) == w) == 1:
                    print(x, y, w, z)

    # ответ yzwx
