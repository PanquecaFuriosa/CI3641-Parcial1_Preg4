from Cuaterniones.Clase import Cuaternion
import math

def test_add_cuaternion():
    resultado = Cuaternion(1, 2, 3, 4) + Cuaternion(2, 3, 4, 5)
    assert resultado.a == 3 and resultado.b == 5 and resultado.c == 7 and resultado.d == 9

def test_add_int():
    resultado = Cuaternion(1, 2, 3, 4) + 5
    assert resultado.a == 6 and resultado.b == 2 and resultado.c == 3 and resultado.d == 4

def test_add_float():
    resultado = Cuaternion(1, 2, 3, 4) + 2.5
    assert resultado.a == 3.5 and resultado.b == 2 and resultado.c == 3 and resultado.d == 4

def test_conjugada():
    resultado = ~Cuaternion(1, 2, 3, 4)
    assert resultado.a == 1 and resultado.b == -2 and resultado.c == -3 and resultado.d == -4

def test_mul_cuaternion():
    resultado = Cuaternion(1, 2, 3, 4) * Cuaternion(2, 3, 4, 5)
    assert resultado.a == -36 and resultado.b == 6 and resultado.c == 12 and resultado.d == 12

def test_mul_int():
    resultado = Cuaternion(3.96, 2, 3, 4) * 8
    assert resultado.a == 31.68 and resultado.b == 2 and resultado.c == 3 and resultado.d == 4

def test_mul_float():
    resultado = Cuaternion(3.96, 2, 3, 4) * 7.5
    assert resultado.a == 29.7 and resultado.b == 2 and resultado.c == 3 and resultado.d == 4

def test_valor_absoluto():
    C = Cuaternion(2, 5, 8, 3)
    resultado = +C
    assert resultado == math.sqrt((C.a**2)+(C.b**2)+(C.c**2)+(C.d**2))

test_add_cuaternion()
test_add_int()
test_add_float()
test_conjugada()
test_mul_cuaternion()
test_mul_int()
test_mul_float()
test_valor_absoluto()