class Capstr(str):
    def __new__(cls,string):
        string=string.upper()
        return super().__new__(cls,string)
d=Capstr("abc")
print(d)
print(d.capitalize())
class C:
    def __init__(self) -> None:
        print("C")
    def __del__(self):
        print("del C")
c=C()
del c
c=C()
d=c
del c
print(d)
class E:
    def __init__(self,name,func) -> None:
        self.name=name
        self.func=func
    def __del__(self):
        self.func(self)
def outer():
    x=0
    def inner(y=None):
        nonlocal x
        if y:x=y
        else:return x
    return inner
f=E("NAME",outer())
del f
class F:
    def __init__(self,name,age):
        self.name=name
        self.__age=age
    def __getattribute__(self, name):
        print("已返回信息")
        return super().__getattribute__(name)
    def __setattr__(self, name, value):
        self.__dict__[name]=value
    def __delattr__(self,name):
        del self.__dict__[name]

g=F("袁宇扬",19)
print(hasattr(g,"name"),hasattr(g,"_F__age"))
setattr(g,"_F__age",19.5)
delattr(g,"_F__age")
print(d.__dict__)
a=NotImplemented