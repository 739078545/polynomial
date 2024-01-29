class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"
   
    def evaluate(self, value):
        return value

class Int:
    def __init__(self, i):
        self.i = i

    def __repr__(self):
        return str(self.i)
    
    def evaluate(self, value):
        return self.i

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)
    
    def evaluate(self, value):
        return self.p1.evaluate(value) + self.p2.evaluate(value)
    
class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return repr(self.p1) + " - " + self._format_p2(self.p2)

    def _format_p2(self, p2):
        if isinstance(p2, (Add, Sub)):
            return "( " + repr(p2) + " )"
        return repr(p2)
    
    def evaluate(self, value):
        return self.p1.evaluate(value) - self.p2.evaluate(value)

class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return self._format_p1(self.p1) + " * " + self._format_p2(self.p2)

    def _format_p1(self, p1):
        if isinstance(p1, (Add, Sub)):
            return "( " + repr(p1) + " )"
        return repr(p1)

    def _format_p2(self, p2):
        if isinstance(p2, (Add, Sub)):
            return "( " + repr(p2) + " )"
        return repr(p2)
    
    def evaluate(self, value):
        return self.p1.evaluate(value) * self.p2.evaluate(value)
    
class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return self._format_p1(self.p1) + " / " + self._format_p2(self.p2)

    def _format_p1(self, p1):
        if isinstance(p1, (Add, Sub, Mul)):
            return "( " + repr(p1) + " )"
        return repr(p1)

    def _format_p2(self, p2):
        if isinstance(p2, (Add, Sub, Mul, Div)):
            return "( " + repr(p2) + " )"
        return repr(p2)
    
    def evaluate(self, value):
        denominator = self.p2.evaluate(value)
        if denominator == 0:
            raise ValueError("Division by zero")
        return self.p1.evaluate(value) / self.p2.evaluate(value)


poly = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))
print(poly)

poly1 = Add(Int(5), Mul(Int(2), X()))
poly2 = Sub(X(), Int(3))
poly3 = Mul(Add(Int(4), X()), Sub(Int(2), X()))
poly4 = Div(Mul(X(), Int(2)), Add(Int(3), X()))
poly5 = Div(Add(X(), Int(1)), Mul(X(), Sub(X(), Int(2))))

print(poly1)  # Expected: "5 + 2 * X"
print(poly2)  # Expected: "X - 3"
print(poly3)  # Expected: "( 4 + X ) * ( 2 - X )"
print(poly4)  # Expected: "( X * 2 ) / ( 3 + X )"
print(poly5)  # Expected: "( X + 1 ) / ( X * ( X - 2 ) )"

poly = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))
print(poly.evaluate(-1))  