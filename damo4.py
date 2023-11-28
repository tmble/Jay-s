def fun(*para):
    print(type(para))
    for item in para:
        print(item)

#调用
fun(10,201,30)
fun([11,25])
#在调用时，参数前加一颗星，分别将列表进行解包
fun(*[10,20,35])

#个数可变的关键字参数
def fun2(**lyx):
    print(type(lyx))
    for key,value in lyx.items():
        print(key,'------',value)

#调用
fun2(name='益旭',age=21,height=173)#关键字参数

d={'name':'益旭','age':18,'height':173}
#fun2(d)#fun2() takes 0 positional arguments but 1 was given
fun2(**d)