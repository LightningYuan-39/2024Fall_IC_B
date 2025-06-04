import time
#用递归跑fib(45)用时78s
def fibiter(i):
    a,b=0,1
    for j in range(i):
        a,b=b,b+a
    return a
start1=time.time()
print(fibiter(150))
end1=time.time()
print(end1-start1)
#同样的功能用迭代连10**-5s都不到
#递归只是代码看上去简单，效率很低
cache=dict()
def fibr_dict(x):
    if x in cache.keys():
        return cache[x]
    else:
        cache[x]=x if x==0 or x==1 else fibr_dict(x-2)+fibr_dict(x-1)
        return cache[x]
start2=time.time()
print(fibr_dict(150))
end2=time.time()
print(end2-start2)
#有递归一定要用dp，否则奇慢
#但是有些问题用不了迭代，只能递归
#函数文档、类型注释、内省
def exchange(dollar,rate=7.01):
    '''
    功能:实现汇率转换将美元转化为人民币
    参数设置
    -dollar:输入的美元数
    -rate:汇率，默认为7.01(2024/9/28)
    返回值：
    人民币的数量
    '''
    rmb=dollar*rate
    return rmb
print(exchange(60,rate=6.32))
def times(n:int,s:str="parking univ.")->str:
    return s*n
print(times(5,"*"))
print(times(5,5))
#类型注释不是给机器看的
print(times(1))
def times(n:int,s=list[int])->list:
    return n*s
print(times.__name__)
print(times.__annotations__)
print(exchange.__doc__)