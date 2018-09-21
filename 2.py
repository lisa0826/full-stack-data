# !/user/bin/env python
# coding:utf8

import sys
reload(sys)
sys.setdefaultencoding('utf8')

c = 'Hello'
d = '你好，世界'


##运算符##
a = {'k1':1,'k2':2,'k3':'Hello'}
b = [1,2,'Hello']

a1 = 1
a2 = 2
a1 += 1

for x in xrange(1,10):
	if x==5:
		continue
		#break 跳出整个循环

print d

import time
e = time.time()
#时间戳的转换

print e #commond+b运行

##文件##
fw = open('data.txt','w')  #写文件w，不断写入文件aw

for x in xrange(1,10):
	fw.write(str(x) + '\n') #str转换字符串

fw.close()


fr = open('data.txt','r')  #读文件

for line in fr:
	print line

#不带换行空格写法
# for line in fr:
# 	line = line.strip()
# 	print line

fr.close()

##异常##
try:
	print 1 / 0
except Exception, e:
	print e
else:
	print 'No Error'
finally:
	print '一定会执行'



##函数##
def Hello(name):
	print 'Hello' + name

Hello('print')






