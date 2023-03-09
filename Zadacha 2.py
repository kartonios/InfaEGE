"""
a= "7"*1000+"3"*1000
while "777" in a or "333" in a:
    a=a.replace("777", "3" , 1)
    a=a.replace("333", "7", 1)
print(a)
"""



"""                                          Задача 1
a="7"*2022
while "777" in a or "333" in a:
    a = a.replace("777", "3", 1)
    a = a.replace("333", "7", 1)
print(a)
"""



"""                                          Задача 2
print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((not x or y) and (x or not z) or w) == 0:
                    print(x,y,z,w)
"""



"""                                          Задача 4
for n in range(0,100):
    r=bin(n)[2:]
    if n % 2== 0:
        r+= '10'
    else:
        r+='11'
    if r.count('1') % 2 == 0:
        r+='0'
    else:
        r+='1'
    res = int(r, base=2)
    if res > 53:
        print(n)
        break
"""



"""                                          Задача 5
for s in range(1, 1000):
    s1 = s
    n = 200
    while s1 > 0:
        s1 = s1 // 4
        n = n - 6
    if n == 170:
        print(s)
        break
"""



"""                                          Задача 9
K - кол-во ячеек под символы
N - кол-во символов доступных для вводы
I - вес всего сообщения
i - степень двойки, способная удовлетворить размеру

N=2**i
I=K*i
"""



"""                                          Задача 10
a = 16**23 + 4**12 - 32**6

s =''

while a > 0:
    s = s+ str(a % 4)
    a = a // 4
print('0', s.count('0'))
print('1', s.count('1'))
print('2', s.count('2'))
print('3', s.count('3'))
print('4', s.count('4'))
"""



"""                                          Задача 11
def f(x, y):
   if x == y:
       return 1
   if x > y or x == 24:
       return 0
   else:
       return f(x+1, y) + f(x*3, y)

print(f(2,12)*f(12,72))
"""


"""                                          Задача 12
for x in range(0,1000):
    x1=x
    L = 0
    M = 0
    while x1 > 0:
        L = L+1
        if M < (x1 % 8):
            M = x1 % 8
        x1 = x1 // 8
    if L == 4 and M == 7:
        print(x)
        print(L)
        print(M)
        break
"""



"""                                          Задача 13"""
def Del(n,m):
    return n%m==0


for A in range(1,10000):
    p = True
    for x in range(1, 100):
        if not(not(Del(x, 54)) or not(Del(x,80))) or not Del(x, A) :
            p = False


    if not p:
        print(A)

"""
def delit(x,y):
    return x%y==0

for a in range(1,1000):
    flag=True
    for x in range(1,1000):
        if not(delit(x,a) or not(delit(x,6)) or not(delit(x,9))):
            flag=False
    if flag:
        print(a)
"""