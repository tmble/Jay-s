import re
pattern='黑客|破解|反爬'
s='我想学习Python,想破解一些vip视频,Python可以实现无底线反爬吗？'
new_s=re.sub(pattern,'***',s)
print(new_s)

s2='https://cn.bing.com/search?q=%E5%88%98%E7%9B%8A%E6%97%AD'
pattern2='[?|%]'
lst=re.split(pattern2,s2)
print(lst)