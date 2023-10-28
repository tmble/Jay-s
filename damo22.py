a={10,20,30}
#向集合中添加元素
a.add(100)
print(a)
#删除元素
a.remove(20)
print(a)
#清空集合中所有元素
#a.clear()
#print(a)

#集合的遍历操作
for item in a:
    print(item)

#使用enumerate()函数
for index,item in enumerate(a):
    print(index,'----->',item)

#集合的生成式
s={i for i in range(1,10)}
print(s)

a={i for i in range(1,10) if i%2==1}
print(a)