import re
pattern='\d\.\d+'
s='I study Python3.11 every day Python2.7 I love you'
match=re.search(pattern,s)
print(match)

s2='T study Python every day'
match2=re.search(pattern,s2)
print(match2)
print(match.group())
#print(match2.group())