fruits=['apple','orange','pear']
counts=[10,3,4]
for f,c in zip(fruits,counts):
    match f,c:
        case 'apple',10:
            print('10个苹果')
        case 'orange',3:
            print('3个橘子')
        case 'pear',4:
            print('4个梨')