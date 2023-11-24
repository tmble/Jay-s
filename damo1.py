def get_sum(num):#num叫形式参数
    s=0

    for i in range(1,num+1):
        s+=i
    print(f'1到{num}之间的累加和为：{s}')

#函数的调用
get_sum(5)#1-5之间的累加和  5是实际参数值
get_sum(100)#1-100之间的累加和  100是实际参数值