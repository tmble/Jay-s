for k in '鹏子哥':
    print(k)
for l in range(3):
        print(l)
for _ in  range(3):
    print('鹏子哥')


sum=0
for k in range(1,101):
    if k %2==0:
        sum+=k
print(sum)

for k in range(100,1000):
    ge=k%10
    shi=k//10%10
    bai=k//100
    #print(bai,shi,ge)
    if bai**3+shi**3+ge**3==k:
      print(k)
