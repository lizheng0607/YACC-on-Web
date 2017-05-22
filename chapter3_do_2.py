##输出10个两位的随机素数
import random
n=0
while n<10:
    x=random.randint(10,99)
    a=2
    while a<x-1:
        if x%2==0:break
        a+=1
    else:
        print(x,end=' ')
        n+=1