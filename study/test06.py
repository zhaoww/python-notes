# -*-coding:utf-8-*-

# list生成式 [expr for iter_var in iterable if cond_expr]
list0 = [x * x for x in (range(1, 10)) if x % 2 == 0]
print(list0)

# 生成器[] -> ()
list1 = (x * x for x in (range(1, 10)) if x % 2 == 0)
print(list1)

for x in list1:
	print(x, end = ' ')

# yield 
# 函数是顺序执行，遇到 return 语句或者最后一行函数语句就返回。而变成 generator 的函数，
# 在每次调用 next() 的时候执行，遇到 yield语句返回，再次执行时从上次返回的 yield 语句处继续执行
def odd():
    print ( 'step 1' )
    yield ( 1 )
    print ( 'step 2' )
    yield ( 3 )
    print ( 'step 3' )
    yield ( 5 )

o = odd()
print( next( o ) )
print( next( o ) )
print( next( o ) )