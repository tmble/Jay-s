s='伟大的中国梦'
#编码str->bytes
scode=s.encode(errors='repalce')#默认是utf-8,因为utf-8中文占3个字节
print(scode)

scode_gbk=s.encode('gbk',errors='replace')#gbk中中文占2个字节
print(scode_gbk)

#编码中的出错问题
s2='耶∴'
scode_errors=s2.encode('gbk',errors='ignore')
print(scode_errors)

#解码过程bytes->str
print(bytes.decode(scode_gbk,'gbk'))
print(bytes.decode(scode,'utf-8'))