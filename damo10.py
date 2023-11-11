import re#导入
patteern='\d.\d+'#+限定符,\d 0-9数字出现1次或多次
s='I study Python3.11 everyday Python2.7 Ilove'
s2='4.10 Python'
s3='I study'
lst=re.findall(patteern,s)
lst2=re.findall(patteern,s2)
lst3=re.findall(patteern,s3)

print(lst)
print(lst2)
print(lst3)