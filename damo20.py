#{}直接创建集合
s={10,20,30,40}
print(s)

#集合只能存储不可变数据类型
#s={[10,20]}#TypeError: unhashable type: 'list'
#print(s)

#使用set()创建集合
s=set()#创建一个空集合,空集合的布尔值是False
print(s)
s={}
print(s,type(s))#dict

s=set('helloworld')
print(s)

s2=set([10,20])
print(s2)

s3=set(range(1,10))
print(s3)

#集合属于序列中的一种
print(min(s3))
print(len(s3))

print(9 in s3)
print(9 not in s3)