try:
    gender=input('请输入你的性别：')
    if gender!='男'and gender!='女':
        raise Exception('未知性别：沃尔玛购物袋')
    else:
        print('你的性别其实是：', gender)
except Exception:
    print(e)