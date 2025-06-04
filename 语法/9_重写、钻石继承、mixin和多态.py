class C:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def mul(self):
        return self.a*self.b
class D(C):
    def  __init__(self,x,y,c):
        C.__init__(self,x,y)
        self.c=c
    def add(self):
        return C.add(self)+self.c
    def mul(self):
        return C.mul(self)*self.c
#传入x,y,c 构造x,y 得到类型里面的a,b
d=D(2,3,4)
print(d.a)
print(d.add())
#钻石继承
class A:
    def __init__(self) -> None:
        print("A")
class B1(A):
    def __init__(self) -> None:
        super().__init__()
        print("B1")
class B2(A):
    def __init__(self) -> None:
        super().__init__()
        print("B2")
class C(B1,B2):
    def __init__(self) -> None:
        super().__init__()
        print("C")
c=C()
del A,B1,B2,C,D
class Displayer:
    def display(self,message):
        print(message)
class LoggerMixin:
    def log(self,message,filename="logfile.txt"):
        with open(filename,"a")as f:
            f.write(message)
    def display(self,message):
        super().display(message)
        self.log(message)
class Mysubclass(LoggerMixin,Displayer):
    def log(self,message):
        super().log(message,filename="subclasslog.txt")
subclass=Mysubclass()
subclass.display("This is a test.")
#需要调用display方法时，找mysubclass再找到loggermixin，找到其中的display函数，根据mro顺序去displayer里面找display，找到displayer的display方法，
#并输出“this is a test.”
#第二句在实例化对象找log方法，就到mysubclass找log方法，把字符串传入，最终创建一个名为subclasslog.txt的文件，写入字符串this is a test.
#也就是super和父类子类没有一点关系，它实际上找的是mro顺序靠后的一方。找方法是先在对象里面找，后在类里面找
import math
class Shape:
    def __init__(self,name) -> None:
        self.name=name
    def area(self):
        pass
class Triangle(Shape):
    def __init__(self,a,b,c) -> None:
        super().__init__("三角形")
        self.a=a
        self.b=b
        self.c=c
    def area(self):
        s=(self.a+self.b+self.c)/2
        area=math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
        return area
class Circle(Shape):
    def __init__(self, r) -> None:
        super().__init__("圆")
        self.r=r
    def area(self):
        return math.pi*(self.r**2)
def area(x):
    return x.area()
c=Circle(6)
t=Triangle(3,4,5)
print(area(c),area(t))
class Pow(Shape):
    def __init__(self,y,a,b) -> None:
        self.y=y
        self.a=a
        self.b=b
    def area(self):
        return (self.b**(self.y+1)-self.a**(self.y+1))/(self.y+1)
m=Pow(2,0,6)
print(area(m))