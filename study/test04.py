# -*-coding:utf-8-*-

# 条件
results = 85

if results > 90:
    print('优秀')
elif results > 80:
    print('良好')
elif results > 60:
    print ('及格')
else :
    print ('不及格') 

# 循环
count = 0
sum = 0
while count < 10:
	if(count % 2 == 0):
		sum += count
	count = count + 1
print(sum)

for x in 'hello':
	print(x)

# for...else
# else 中的语句会在循环正常执行完（即 for 不是通过 break 跳出而中断的）的情况下执行
for num in range(10,20):  # 迭代 10 到 20 之间的数字
    for i in range(2,num): # 根据因子迭代
        if num%i == 0:      # 确定第一个因子
        	j=num/i          # 计算第二个因子
        	print ('%d 是一个合数' % num)
        	break            # 跳出当前循环
    else:                  # 循环的 else 部分
        print ('%d 是一个质数' % num)

# while...else 同理