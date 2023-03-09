'Задача 13'
# p = 'АВД БАД ВГ ГДЖ ДВЖ ЕБДЖ ЖИКМ ИЕ КИМ ЛГ МЛ'
# d = {c[0]: c[1:] for c in p.split()}
#
# def step(s, end):
#     if s[-1] == end and len(s) > 1:
#         return 1
#     else:
#         return sum(step(s+c, end) for c in d[s[-1]] if c not in s[1:])
#
#
# print(step('Д', 'Д'))


'Задача 13'
# p = 'АБ БВ ВГЕЖ ГИ ДА ЕАД ЖЕГ ИМН КДЖ ЛЖК МЖЛ НМ'
# d = {c[0]: c[1:] for c in p.split()}
#
# def step(s, end):
#     if s[-1] == end and len(s) > 1:
#         return 1
#     else:
#         return sum(step(s+c, end) for c in d[s[-1]] if c not in s[1:])
#
# print(step('Е', 'Е'))

for a in range(10):
    for b in range(10):
        if (a+b)*(a-b)*a*b == 2016:
            print(a, b)