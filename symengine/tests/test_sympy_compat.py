from symengine.sympy_compat import (Integer, Rational, S, Basic, Add, Mul,
    Pow, symbols, Symbol, log, sin, zeros, atan2)

def test_Integer():
    i = Integer(5)
    assert isinstance(i, Integer)
    assert isinstance(i, Rational)
    assert isinstance(i, Basic)
    assert i.p == 5
    assert i.q == 1

def test_Rational():
    i = S(1)/2
    assert isinstance(i, Rational)
    assert isinstance(i, Basic)
    assert i.p == 1
    assert i.q == 2

def test_Add():
    x, y = symbols("x y")
    i = Add(x, x)
    assert isinstance(i, Mul)
    i = Add(x, y)
    assert isinstance(i, Add)
    assert isinstance(i, Basic)

def test_Mul():
    x, y = symbols("x y")
    i = Mul(x, x)
    assert isinstance(i, Pow)
    i = Mul(x, y)
    assert isinstance(i, Mul)
    assert isinstance(i, Basic)

def test_Pow():
    x = symbols("x")
    i = Pow(x, 1)
    assert isinstance(i, Symbol)
    i = Pow(x, 2)
    assert isinstance(i, Pow)
    assert isinstance(i, Basic)

def test_sin():
    x = symbols("x")
    i = sin(0)
    assert isinstance(i, Integer)
    i = sin(x)
    assert isinstance(i, sin)

def test_log():
    x, y = symbols("x y")
    i = log(x, y)
    assert isinstance(i, Mul)
    i = log(x)
    assert isinstance(i, log)

def test_ATan2():
    x, y = symbols("x y")
    i = atan2(x, y)
    assert isinstance(i, atan2)
    i = atan2(0, 1)
    assert i == 0

def test_zeros():
    assert zeros(3, c=2).shape == (3, 2)

def test_has_functions_module():
    import symengine.sympy_compat as sp
    assert sp.functions.sin(0) == 0
