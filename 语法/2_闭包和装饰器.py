#闭包
def fun1():
    x=1
    def fun2():
        print(x)
    return fun2
fun1()()
'''
fun1()=fun2,fun1()()=fun2()=1
电脑看到def,不执行操作直到第6行结束
看到fun1()调用fun1,令x=1,看到def不执行操作,直到最后,返回值为fun2
故fun1()=fun2,此时电脑在第六行,回头找fun2,把x打印出来,并不返回任何值
x=1,所以最后输出的值为1
'''
fun3=fun1()
def fun1():
    pass
fun3()
'''
第15行中,fun3=fun1()fun3拿到的不是调用fun1的渠道,而是里面的所有代码,所以当我们取消fun1时,fun3可以保留这些代码
'''
def outer():
    x=0
    y=0
    def inner(x1,y1):
        nonlocal x,y
        x+=x1
        y+=y1
        print(f"现在x={x},y={y}")
    return inner
move=outer()
move(1,2)
move(-2,2)
'''
内层函数能记住外层函数的作用域
'''
#装饰器
import time
def timemgr(func):
    def call():
        print("开始调用函数")
        start=time.time()
        func()
        end=time.time()
        print(f"函数调用完毕,一共执行{(end-start):.3f}秒")
    return call
@timemgr
def func1():
    time.sleep(2.024)
    print("正在调用函数func1")
def func2():
    time.sleep(0.808)
    print("正在调用函数func2")
func1()
func2()
'''
装饰器的好处，在于可以在定义函数时自动调用
装饰器只管一个函数,不要手动取消
'''
def add(func):
    def inner1():
        x=func()
        return x+1
    return inner1
def square(func):
    def inner2():
        x=func()
        return x**2
    return inner2
def cube(func):
    def inner3():
        x=func()
        return x**3
    return inner3
#装饰器的叠加遵循就近原则
@cube
@square
@add#func3()=add(func3())
def func3():
    return 2
print(func3())
#给装饰器传递参数
import time
def sysinfo(msg):
    def time_master(func):
        def call_func():
            start=time.time()
            time.sleep(1)
            func()
            print(f"正在执行函数{msg}")
            end=time.time()
            print(f"执行时间为{end-start:.3f}秒")
        return call_func
    return time_master
@sysinfo(msg="A")
def funca():
    print("开始执行函数A")
@sysinfo(msg="B")
def funcb():
    print("开始执行函数B")
funca()
funcb()