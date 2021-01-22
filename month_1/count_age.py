# 除法运算符 /
a = 10
b = 2
print(a / b)

# 向下取证运算符 //
a = 9
b = 3
print(a / b)
# 3.0
print(a // b)
# 3

# 余数运算符
print(10 / 3)  # 3.3333333333333335
print(10 % 3)  # 1
print(3 / 10)  # 0.3
print(3 % 10)  # 3
print(-10 % 3)  # r=-10+12 =2
print(10 % -3)  # r=10-12= -2

# 赋值运算符
a = b = 5
print(a, b)  # 5 5
a, b = 5, 10
print(a, b)  # 5 10
# a,b位置互换
a, b = b, a
print(a, b)
# 10 5

# 复合赋值运算符
a = 5
a += 2  # a=5+2=7
print(a)

b = 10
b *= 2
print(b)  # 20
