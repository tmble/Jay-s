def calc(a,b):
    return a+b

print(calc(10,20))

#匿名函数
s=lambda a,b:a+b#s表示就是一个匿名函数
print(type(s))#<class'function'>
#调用匿名函数
print(s(10,20))
print('-'*30)
#列表的正常取值操作
lst=[10,20,30,40,50]
for i in range(len(lst)):
    print(lst[i])
print('-'*30)
for i in range(len(lst)):
    result=lambda x:x[i]#根据索引取值，result类型是function，x是形式参数
    print(result(lst))#lst是实际参数
print('-'*30)
student=[
    {'name':'鹏子一号','score':98},
    {'name': '鹏子二号', 'score': 97},
    {'name': '鹏子三号', 'score': 92},
    {'name': '鹏子四号', 'score': 94}
]
#对列表进行排序,排序的规则是字典的成绩
student.sort(key=lambda x:x.get('score'),reverse=True)#降序
print(student)