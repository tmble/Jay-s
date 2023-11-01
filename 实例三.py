#创建字典用于存储车票信息,使用车次作key,使用其他信息作value
dict_ticket={
    'G1569':['成都东-达州','18:06','18:39','00:33'],
    'G1567':['成都东-达州','18:15','18:49','02:33']
}
print('车次       出发站-到达站         出发时间        到达时间          历时时长')
#遍历字典中的元素
for key in dict_ticket.keys():
    print(key,end=' ')#为啥不换行，因为车次和车次的详细信息在一行显示
    #根据key获取出来的值是一个列表,
    for item in dict_ticket.get(key):#根据key获取值
        print(item,end='\t\t\t\t')
    #换行
    print()
#输入拥护的购票车次
train_no=input('请输入要购买的车次：')
#根据key值获取值
info=dict_ticket.get(train_no,'车次不存在')#info是一个列表类型
#判断车次是否存在
if info!='车次不存在':
    person=input('请输入乘车人,如果多位乘车人使用逗号分割：')
    #获取车次的出发站-到达站，还有出发时间
    s=info[0]+' '+info[1]+'开'
    print('您已购买了'+train_no+s+'请'+person+'尽快换取纸质车票.[铁路客服]')
else:
    print('对不起，选择的车次不存在')
