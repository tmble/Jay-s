class Student:
    school='成都xxx教育'
    def __init__(self,xm,age):
        self.name=xm
        self.age=age
    def show(self):
        print(f'我叫：{self.name},今年:{self.age}岁了')

stu=Student('lyx',age=21)
stu2=Student('刘益旭',20)
print(stu.name,stu.age)
print(stu2.name,stu2.age)

#为stu2动态绑定一个实例属性
stu2.gender='♂'
print(stu2.name,stu2.gender)

#动态绑定方法
def introduce():
    print('我是一个普通的函数，我被动态绑定成了stu2对象的方法')
stu2.fun=introduce#函数的一个赋值
#fun就是stu2对象的方法
#调用
stu2.fun()