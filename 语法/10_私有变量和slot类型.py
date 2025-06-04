class Cat:
    def __init__(self,color,ability) -> None:
        self.__color=color
        self.__ability=ability
    def set(self,color,ability):
        self.__color=color
        self.__ability=ability
    def get_color(self):
        print(self.__color)
    def __say(self):
        print("我会抓老鼠")
    def __can_catch_mice(self):
        return self.__ability
b=Cat("白",True)
b.get_color()
b.set("黑",False)
b.get_color()
print(b.__dict__)
print(b._Cat__color)
print()
b._Cat__say()
print(b._Cat__can_catch_mice())
b.__is_blind=True
print(b.__dict__)
#名字改编只会发生在类实例化对象的时候的事情
print(Cat.__dict__)
b.__dict__["property_"]="*"
print(b.__dict__)
#slot属性，避免字典浪费内存
class C:
    __slots__=["x","y"]
    def __init__(self,x,y):
        self.x=x
        self.y=y
c=C(250,520)
print(c.x,c.y)
class E(C):
    pass
e=E(250,520)
e.z=666
print(e.__slots__)
print(e.__dict__)