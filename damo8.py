lst=['hello','world','python','p2p']
for item in lst:
    print(item)
for i in range(0,len(lst)):
    print(i,'--->',lst[i])

for index,item in enumerate(lst):
    print(index,item)
for index,item in enumerate(lst,start=66):
    print(index,item)
for index,item in enumerate(lst,99):
    print(index, item)