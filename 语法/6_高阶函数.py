import functools
jiecheng=lambda x:functools.reduce(lambda x,y:x*y,range(1,x+1))
print(jiecheng(5))
square=functools.partial(pow,exp=2)
print(square(1.5))
from time import *
def timemgr(func):
    @functools.wraps(func)
    def call_func():
        print("开始运行程序")
        start=time()
        func()
        end=time()
        print("结束程序运行")
        print(f"该程序一共运行{end-start:.5f}秒")
    return call_func
@timemgr
def func01():
    sleep(1.00000)
    print("*")
func01()
print(func01.__name__)
