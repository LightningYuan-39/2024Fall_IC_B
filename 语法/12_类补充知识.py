class Rational:
    @staticmethod
    def _gcd(m,n):
        if n==0:m,n=n,m
        while m!=0:
            m,n=n%m,m
        return n
    def __init__(self,x,y=1):
        if not isinstance(x,int) or not isinstance(y,int):
            raise TypeError
        if y==0:
            raise ZeroDivisionError
        sign=1
        if x<0:x,sign=-x,-sign
        if y<0:y,sign=-y,-sign
        g=Rational._gcd(x,y)
        self._num=sign*(x//g)
        self._den=y//g
    @property
    def num(self):
        return self._num
    @property
    def den(self):
        return self._den
    def __str__(self):
        return f"{self._num}/{self._den}"
    def __add__(self,another):
        if isinstance(another,int):
            another=Rational(another)
        return Rational(self.num*another.den+self.den*another.num,another.den*self.den)
    def __hash__(self):#不变对象才能哈希
        return hash((self.num,self.den))
    def __eq__(self,another):
        if isinstance(another,int):
            another=Rational(another)
        return another.num*self.den==self.num*another.den
    def print(self):
        print(f"{self.num}/{self.den}")
class Matrix(list):
    def transpose(self):
        return Matrix(list(i) for i in zip(self))
if __name__=="__main__":
    a=Rational(-2,-4)
    print(f"{a.__hash__()=}")
    b=Rational(3,9)
    c=Rational(3,6)
    print(a==c)
    d=a+b
    d.print()
    print(Rational.__str__(a))
    import decimal
    print(decimal.__doc__)
