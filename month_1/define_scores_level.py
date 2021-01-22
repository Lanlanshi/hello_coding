#method 1
#打开文件
file_source=open('scores.text','r') #r模式，文件不存在的时候报错

#操作文件
score_line= file_source.readline()
while score_line !='':
    print(score_line,end='')
    score_line=file_source.readline()

#关闭文件
file_source.close()






#
score_lines=file_source.readlines()
# print(score_lines) #['刘秀  50\n', '蒋云姣 90\n', '史兰兰 79\n', '刘宁  65\n', '谢远发 50\n', '许翠云 85']

for line in score_lines:
    print(line,end='')