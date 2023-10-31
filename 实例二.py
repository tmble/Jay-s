#创建一个空列表，用于存储入库的商品信息
lst=[]
for i in range(5):
    goods=input('输入商品编号和名称入,每次只能输一次：')
    lst.append(goods)
#输出所有商品信息
for item in lst:
    print(item)
#创建一个空列表，用于存储购物车中的商品
cart=[]
while True:
    flag=False#代表没有商品入库
    num=input('输入商品编号：')
    #遍历商品列表，查询一下要购买的商品是否存在
    for item in lst:
        if num==item[0:3]:#切片操作，从商品中切出序号
            flag=True#代表商品已找到
            cart.append(item)#添加到购物车中
            print('商品已成功添加到购物车中')
            break#退出的是for循环
    if not flag and num!='q':#not flag 等价于flag==False
        print('商品不存在')

    if num=='q':
        break#退出的才是while循环
print('-'*50)
print('您购物车里已选择的商品为：')
cart.reverse()
for item in cart:
    print(item)