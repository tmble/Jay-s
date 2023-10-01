answer=input('你是鹏子哥吗？yes/no')
money=float(input('请输入购物金额'))
if answer=='yes':
    if money>=200:
        print('买的不错，打八折，下次多买点：',money*0.8)
    elif money>=100:
        print('有点少哦，这次打九折：',money*0.9)
    else:
        print('买这么少，打你妹的折：',money)
else:
    if money>=200:
        print('下次多买点,这次打九五折：',money*0.95)
    else:
        print('买这么少，还想打折：',money)