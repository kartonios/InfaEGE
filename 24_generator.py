import random
from random import *
import re

# прочитать файл и найти в нем такое число, записанное в десятичной системе,
# у которого в 14-ричной записи будет наибольшее число цифр A. Если таких чисел
# несколько, вывести максимальное из них. A1A, AA1 -> AA1_14 = 10*14^2 + 10*14 + 1 = 1960+140+1=2101
#
# with open('24_hex.txt', 'w') as f:
#     print(''.join(choices('0123456789_!@#$%^&*(){}[]', k=100000)), file=f)

s = open(r'24_hex.txt').read()
maxW = 0
maxM = 0
maxM14 = ''
a = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'A', 11:'B', 12:'C', 13:'D'}
for m in re.findall('\d+',s):
    res =[]
    d14 = []
    n = int(m, 10)
    n2 = n
    while n > 0:
        res.append(n % 14)
        d14.insert(0, a[n % 14])
        n //= 14

    n14 = ''.join(d14)
    if res.count(10) > maxW:
        maxW = res.count(10)
        maxM14 = n14
        maxM = n2
    elif res.count(10) == maxW:
        if n2 > maxM:
            maxM14 = n14
            maxM = n2

print(maxM14, maxW)
