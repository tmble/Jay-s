lst=[
    ['01','鹏子哥的笔','九阳',500],
    ['02','鹏子哥的本','美的',1000],
    ['03','鹏子哥的电脑','联想',400],
]
print('编号\t\t名称\t\t\t\t品牌\t\t单价')
for item in lst:
    for i in item:
        print(i,end='\t\t')
    print()#换行
#格式化
for item in lst:
    item[0]='0000'+item[0]
    item[3]='￥{0:.2f}'.format(item[3])

print('编号\t\t\t名称\t\t\t\t品牌\t\t单价')
for item in lst:
    for i in item:
        print(i,end='\t\t')
    print()#换行