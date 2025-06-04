#lambda表达式是函数的简化版本,其基本形式为：
#lambda arg1,arg2,argn:expression
square=lambda x: x**2
print(square(3))
z=[lambda x:x**2,2,3]
print(z[0](z[2]))
mapped=map(lambda x:ord(x)+10,"VSCode")
print(list(mapped))
def counter():
    i=0
    while i<=5:
        yield i
        i+=1
for j in counter():
    print(j)
c=counter()
print(c)
for k in range(6):
    print(next(c))#相当于每写一次next(c)都调用一次生成器，直到迭代结束。
#所以不能用索引的方式获取参数，如c[2]
#原代码
def outer():
    a=0
    b=1
    def inner():
        nonlocal a,b
        print(a)
        c=a
        a=b
        b+=c
    return inner
move=outer()
for i in range(10):
    move()
#使用生成器实现
def outer():
    a,b=0,1
    i=0
    while True:
        yield a
        a,b=b,b+a
f=outer()
for i in range(10):
    print(next(f))
#使用递归实现
def fib(x):return x if x==1 or x==0 else fib(x-1)+fib(x-2)
for i in range(10):print(fib(i))