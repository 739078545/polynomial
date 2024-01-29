class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"

class Int:
    def __init__(self, i):
        self.i = i

    def __repr__(self):
        return str(self.i)

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)
    
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


poly = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))
print(poly)