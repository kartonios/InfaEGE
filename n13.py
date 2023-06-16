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

'Задача 13'

# path = "АБ БВЕД ВГЖИ ГИ ДА ЕВЛЖ ЖЛ ИМН КД ЛДК МЖЛ НМ"
# d = {x[0]: x[1:] for x in path.split()}
#
# def f(s, end):
#     if s[-1] == end and len(s) > 1:
#         return 1
#     else:
#         return sum(f(s+c, end) for c in d[s[-1]] if c not in s[0:])
#
# print(f('Е', 'Ж'))


'Задача 13 статград'
# path = "АБ БВЕ ВГИЖ ГИ ДАБ ЕВДЛ ЖЕМ ИЖН КД ЛДК МИЕЛ НМ"
# d = {x[0]: x[1:] for x in path.split()}
#
# def f(s, end):
#     if s[-1] == end:
#         return 1
#     return sum(f(s+c, end) for c in d[s[-1]] if c not in s[0:])
#
# print(f("А", "Н"))

# 6

path = "АБГ БЕВ ВЗД ГВДЖ ДЗИЖ ЕКМ ЖИЛ ЗЕИМ ИЛ КМ ЛМ М"

d = {n[0]: n[1:] for n in path.split()}

def go(s, end):
    if s[-1] == end and len(s) > 1:
        return 1
    else:
        return sum(go(s+c, end) for c in d[s[-1]] if c not in s[0:])

print(go('А', 'З')*go('З', 'М'))
