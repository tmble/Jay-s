d={10:'cat',20:'dog',30:'pet',20:'zoo','a':40}
#访问字典中的元素
#（1)使用d[key]
print(d['a'])
#(2)d.get(key)
print(d.get('a'))

#二者之间是有区别的，如果key不存在，d[key]报错d.get(key)可以指定默认值
#print(d['b'])#KeyError: 'b'
print(d.get('b'))#None
print(d.get('b','不存在'))

#字典的遍历
for item in d.items():
    print(item)#key=value组成的一个元素

#在使用for循环遍历时，分别获得key,value
for key,value in d.items():
    print(key,'---->',value)