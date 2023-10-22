d={10:'cat',20:'dog',30:'pet',20:'zoo'}
print(d)#key相同时，value值进行了覆盖


lst1=[10,20,30,40]
lat2=['cat','dor','koh','huh','jij']
a=zip(lst1,lat2)
print(a)#<zip object at 0x000002F0E1767000>
#print(list(a))#[(10, 'cat'), (20, 'dor'), (30, 'koh'), (40, 'huh')]
d=dict(a)
print(d)#{10: 'cat', 20: 'dor', 30: 'koh', 40: 'huh'}

#使用参数创建字典
d=dict(cat=10,dog=20)#左侧cat是key,右侧是value
print(d)

t=(10,20,30)
print({t:10})#t是key,10是value,元组是可以作为字典中的key
#字典属于序列
print('max:',max(d))
print('min:',min(d))
print('len:',len(d))
#del d
print(d)