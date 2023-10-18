lst=[
    ['城市','环比','同比'],
    ['北京',102,103],
    ['上海',101,135],
    ['深圳',156,488]
]
print(lst)
for row in lst:
    for item in row:
        print(item,end='\t')
    print()
lst2=[[j for j in range(5)]for i in range(4)]
print(lst2)
for row in lst2:
    for item in row:
        print(item,end='\t')
    print()