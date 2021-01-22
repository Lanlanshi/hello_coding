seconds=int(input('请输入秒数'))
second=seconds%60
minutes=seconds//60
hour=minutes//60
minute=minutes%60
print('转化以后的结果是：',hour,'小时',minute,'分钟',second,'秒')