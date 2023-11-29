def calc(a,b):
    print(a+b)

calc(10,20)
print(calc(1,2))#none

def calc2(a,b):
    s=a+b
    return s#将s返回给函数的调用处去处理
print('-'*10)
get_s=calc2(1,2)
print(get_s)

get_s2=calc2(calc2(1,2),3)#1+2+3
print(get_s2)

#返回值可以是多个
def sum(num):
    s=0#累加和
    b=0#奇数和
    c=0#偶数和
    for i in range(1,num+1):
        if i%2!=0:#说明是奇数
            b+=i
        else:
            c+=i
        s+=i
    return b,c,s#三个值

result=sum(10)
print(type(result))
print(result)

#解包赋值
a,b,c=sum(10)#返回3个值,元组类型
print(a)
print(b)
print(c)