import random
lst=[item for item in range(1,16)]
print(lst)
lst=[item*item for item in range(1,16)]
print(lst)
lst=[random.randint(1,100) for _ in range(1,16)]
print(lst,id(lst))
lst=[i for i in range(10) if i%2==0]
print(lst)