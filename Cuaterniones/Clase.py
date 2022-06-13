from __future__ import annotations
import math

"""
 Clase que que implementa la estructura matemática cuaternión
 con las operaciones básicas.
 Autor: Gabriela Panqueva 06/2022.
"""
class Cuaternion:
    
    """
     Función que sobreescribe la inicialización de un cuaternión al ser creado.
     Se le asignan las componentes a, bi. cj y dk.
     Argumentos:
     self: El propio cuaternión.
     a: Int, componente a del cuaternión.
     b: Int, componente b del cuaternión.
     c: Int, componente c del cuaternión.
     d: Int, componente d del cuaternión.
     Autor: Gabriela Panqueva 06/2022.
    """
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    
    """
     Función que sobreescribe el método biádico del operador (+) para la implementación
     de la suma de cuaterniones y de un cuaternión con un número real.
     Argumentos:
     self: El propio cuaternión.
     other: El otro elemento al que se le aplicará la suma.
     Retorna:
     Un nuevo cuaternión, producto de la suma realizada.
     Autor: Gabriela Panqueva 06/2022.
    """
    def __add__(self, other) -> Cuaternion:
        if (type(other) is int or type(other) is float):
            return Cuaternion((self.a + other), self.b, self.c, self.d)
        elif (type(other) is Cuaternion):
            return (Cuaternion((self.a + other.a), (self.b + other.b), (self.c + other.c), (self.d + other.d)))

    """
     Función que sobreescribe el método biádico del operador (*) para la implementación
     de la multiplicación de cuaterniones y de un cuaternión con un número real.
     Argumentos:
     self: El propio cuaternión.
     other: El otro elemento al que se le aplicará la multiplicación.
     Retorna:
     Un nuevo cuaternión, producto de la multiplicación realizada.
     Autor: Gabriela Panqueva 06/2022.
    """
    def __mul__(self, other) -> Cuaternion:
        if (type(other) is int or type(other) is float):
            return Cuaternion((self.a * other), self.b, self.c, self.d)
        elif (type(other) is Cuaternion):
            return (Cuaternion((self.a * other.a) - (self.b * other.b) - (self.c * other.c) - (self.d * other.d),
                            (self.a * other.b) + (self.b * other.a) + (self.c * other.d) - (self.d * other.c),
                            (self.a * other.c) - (self.b * other.d) + (self.c * other.a) + (self.d * other.b),
                            (self.a * other.d) + (self.b * other.c) - (self.c * other.b) + (self.d * other.a)))
    """
     Función que sobreescribe el método monádico del operador (+) para la implementación
     de la medida o valor absoluto de un cuaternión.
     Argumentos:
     self: El propio cuaternión.
     Retorna: 
     El punto flotante resultante de la operación.
     Autor: Gabriela Panqueva 06/2022.
    """
    def __pos__(self) -> float:
        return round(math.sqrt((self.a*self.a)+(self.b*self.b)+(self.c*self.c)+(self.d*self.d)), 2)

    """
     Función que sobreescribe el método monádico del operador (~) para la implementación
     de la conjugada de un cuaternión.
     Argumentos:
     self: El propio cuaternión.
     Retorna: 
     El cuaternión que representa la conjugada del cuaternión dado.
     Autor: Gabriela Panqueva 06/2022.
    """
    def __invert__(self) -> Cuaternion:
        return (Cuaternion(self.a, self.b*-1, self.c*-1, self.d*-1))