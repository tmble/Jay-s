import random
d={item:random.randint(1,1000) for item in range(4)}
print(d)

#创建两个元素
lst=[1001,1002,1003]
lst2=['陈东东','网鹏','喷这个']
d={key:value for key,value in zip(lst,lst2)}
print(d)