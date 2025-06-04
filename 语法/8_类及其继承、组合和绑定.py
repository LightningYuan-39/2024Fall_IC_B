class Turtle:
    legs=4
    shell=True
    def sleep(self):
        print("Zzzz……")
t1=Turtle()
print(t1.legs)
t2=Turtle()
t2.legs=3
print(t2.legs)
print(t1.legs)
t1.mouth=1
print(t1.mouth)
print(dir(t1))
class c:
    def get_self(self):
        print(self)
c1=c()
c1.get_self()
#继承
class A:
    x=520
    def hello(self):
        print("A")
class B(A):
    pass
b=B()
b.hello()
print(b.x)
class B(A):
    x=2024
a=A()
print(a.x)
b=B()
print(b.x)
print(isinstance(b,A))
print(issubclass(B,A))
class B:
    x=150
    def hello(self):
        print("B")
class C(B,A):
    pass
a=C()
print(a.x)
a.hello()
#当多重继承的属性和方法互相冲突时，取写在前面的一个
class A:
    def say(self):
        print("A")
class B:
    def say(self):
        print("B")
class C:
    def say(self):
        print("C")
class Total:
    a=A()
    b=B()
    c=C()
    def say(self):
        self.a.say()
        self.b.say()
        self.c.say()
d=Total()
d.say()
class C:
    def get_self(self):
        print(self)
c=C()
c.get_self()
#类具有属性和方法，当它产生时,它先有自己的属性和方法，再按顺序继承父类的各种属性和方法；
#当一个对象属于类，当它调用属性时，先调用自己的属性，再调用类的属性；当它在调用方法时，调用类的方法，并将自己作为参数传入。
class C:
    def set_x(self,v):
        self.x=v
c=C()
c.set_x(250)
print(c.x)
class C:
    x=100
    def set_x(self,v):
        x=v
c=C()
C.x=250
print(c.x)
c.__dict__
del C,c
#空类可以当字典使用
class C:
    pass
C.x=150
C.y="Python"
C.z=[1,2,3]
#但是这个字典只能由键找值，不能由值找键
