def happy(name='益旭',age=21):
    print('祝'+name+'生日快乐')
    print(str(age)+'岁生日快乐')

#调用
happy()#不用传参
happy('鹏子')#位置传参
happy(age=133)#关键字传参，name采用默认值

happy(19)#19会被赋给name

def fun(a,b=20):#a为位置参数，b默认值参数
    pass

#def fun2(a=20,b):#同时存在时，位置参数在后会报错
#当位置参数和关键字参数同时存在时，应位置参数在前，默认参数在后