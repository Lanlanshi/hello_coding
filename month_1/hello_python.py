print('hello world')
# hello world

#输出变量
price=10
number=5
print(price)
# 10
print(price,number)
# 10 5
print('总共消费',number*price)
# 总共消费 50

#分隔符
print('hello','world')
# hello world
# 注释一行代码快捷键command+/
# 复制一行代码快键键command+d
print('hello','world',sep=',')
# hello,world
print('2021','01','21',sep='-')
# 2021-01-21
print('125121126','qq.com',sep='@')
# 125121126@qq.com

print('hello',end='')#end表示下一个连续输入
print('world')
# helloworld
print('hello',end='\n')
print('world')
# helloworld
print('hello',end='\n\n\n\n\n')
print('world')
print('hello',end='/n')
print('world')
# hello/nworld

# file
file_source=open('zen.text','w')
print('人生苦短，我用Python',file=file_source)
file_source.close()




