# -*- coding: utf-8 -*-

# 判断正整数
a = 12
# 居然用: 搞得第一次编译就报错了
if a >= 0:
	print('yes')
else:
	print('no')

# 转义 \
print('\'hello \n python\'')
# 去除转义 r
print(r'\n---')
# 多行
print(r'''hello
'python'
"haha中文"''')